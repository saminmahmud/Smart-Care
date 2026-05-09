import stripe
from datetime import date, datetime, timedelta
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.decorators import doctor_required
from appointments.models import Appointment, Payment
from doctors.forms import DoctorProfileForm
from doctors.models import Doctor, DoctorSchedule, Review, Specialization
from django.db.models import Q, Avg, Count, Max, Sum
from django.core.paginator import Paginator
from django.contrib import messages
from doctors.utils import generate_transaction_id, get_daily_slots
from patients.models import Patient
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from calendar import month_abbr
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


def doctors_list_view(request):
    available_today = request.GET.get('available_today', '') == 'true'
    consultation_fee = request.GET.get('consultation_fee', '')
    rating = request.GET.get('rating', '')
    experience = request.GET.get('experience', '')
    sort = request.GET.get('sort', 'recommended')
    search_query = request.GET.get('search', '')
    specialization_id = request.GET.get('specialization', '')

    doctors = Doctor.objects.select_related('user', 'specialization', 'designation').prefetch_related('reviews').all()
    specializations = Specialization.objects.all()

    # Search filter
    if search_query:
        doctors = doctors.filter(
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(hospital_name__icontains=search_query) |
            Q(specialization__name__icontains=search_query) |
            Q(designation__name__icontains=search_query)
        )

    # Specialization filter
    if specialization_id:
        doctors = doctors.filter(specialization__id=specialization_id)

    # Available today filter
    if available_today:
        today_weekday = datetime.now().strftime('%A')
        doctors = doctors.filter(
            schedules__day_of_week__iexact=today_weekday,
            schedules__is_active=True
        ).distinct()

    # Consultation fee filter
    if consultation_fee:
        try:
            fee_val = int(consultation_fee)
            doctors = doctors.filter(consultation_fee__lte=fee_val)
        except ValueError:
            pass

    if rating:
        try:
            rating_val = float(rating)
            doctors = doctors.annotate(
                avg_rating_val=Avg('reviews__rating')
            ).filter(avg_rating_val__gte=rating_val)
        except ValueError:
            pass
    else:
        doctors = doctors.annotate(avg_rating_val=Avg('reviews__rating'))

    # Experience filter
    if experience:
        try:
            exp_val = int(experience)
            doctors = doctors.filter(experience_years__gte=exp_val)
        except ValueError:
            pass

    # Sorting
    if sort == 'low_to_high':
        doctors = doctors.order_by('consultation_fee')
    elif sort == 'high_to_low':
        doctors = doctors.order_by('-consultation_fee')
    elif sort == 'experience':
        doctors = doctors.order_by('-experience_years')
    else:  # recommended
        doctors = doctors.order_by('-avg_rating_val', '-experience_years')

    doctors = doctors.distinct()

    # Pagination
    paginator = Paginator(doctors, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    query_params.pop('page', None)

    context = {
        'doctors': page_obj,
        'page_obj': page_obj,
        'specializations': specializations,
        'available_today': available_today,
        'consultation_fee': consultation_fee,
        'rating': rating,
        'experience': experience,
        'sort': sort,
        'search_query': search_query,
        'specialization_id': specialization_id,
        'query_params': query_params.urlencode(), 
    }

    return render(request, 'pages/doctor.html', context)


def doctor_details_view(request, doctor_id):
    doctor = get_object_or_404(
        Doctor.objects.select_related('user', 'specialization', 'designation').prefetch_related('reviews', 'schedules'),
        id=doctor_id
    )
    today = date.today()
    max_date = today + timedelta(days=7)
    
    if request.method == 'POST':
        try:
            patient = request.user.patient
        except Exception:
            messages.error(request, "Only patients can book appointments.")
            return redirect('doctor_details', doctor_id=doctor.id)

        slot_str = request.POST.get("selected_slot")
        appointment_date_str = request.POST.get("selected_date")

        if not slot_str or not appointment_date_str:
            messages.error(request, "Please select a date and time slot.")
            return redirect('doctor_details', doctor_id=doctor.id)

        try:
            start_time = datetime.strptime(slot_str, "%H:%M").time()
            appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date or time.")
            return redirect('doctor_details', doctor_id=doctor.id)

        if appointment_date < today or appointment_date > max_date:
            messages.error(request, "You can only book within the next 7 days!")
            return redirect('doctor_details', doctor_id=doctor.id)

        day_name = appointment_date.strftime("%A")
        schedule = doctor.schedules.filter(day_of_week=day_name, is_active=True).first()
        if not schedule:
            messages.error(request, f"Doctor is not available on {day_name}.")
            return redirect('doctor_details', doctor_id=doctor.id)

        valid_slots = get_daily_slots(doctor, appointment_date)
        valid_times = [s['slot'] for s in valid_slots]
        if start_time not in valid_times:
            messages.error(request, "Invalid slot selected.")
            return redirect('doctor_details', doctor_id=doctor.id)

        if Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            start_time=start_time,
            status='scheduled'
        ).exists():
            messages.error(request, "Sorry, this slot is already booked!")
            return redirect('doctor_details', doctor_id=doctor.id)

        end_time = (
            datetime.combine(appointment_date, start_time) +
            timedelta(minutes=schedule.slot_duration)
        ).time()

        new_appointment = Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            start_time=start_time,
            end_time=end_time,
        )
        new_payment = Payment.objects.create(
            appointment=new_appointment,
            amount=doctor.consultation_fee,
            transaction_id=generate_transaction_id(),
            status='pending'
        )
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'bdt',
                        'product_data': {
                            'name': 'Consultation Fee',
                        },
                        'unit_amount': int(doctor.consultation_fee * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse("my_appointments")
            ) + f"?success=1&payment_id={new_payment.id}",

            cancel_url=request.build_absolute_uri(
                reverse("my_appointments")
            ) + f"?canceled=1&payment_id={new_payment.id}",
            metadata={'payment_id': new_payment.id}
        )
        new_payment.stripe_session_id = checkout_session.id
        new_payment.save()

        return redirect(checkout_session.url, code=303)

    reviews = doctor.reviews.all()
    schedules = doctor.schedules.filter(is_active=True)

    date_str = request.GET.get('selected_date')
    try:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if selected_date < today or selected_date > max_date:
            selected_date = today
    except (ValueError, TypeError):
        selected_date = today

    slots = get_daily_slots(doctor, selected_date)

    available_days = list(schedules.values_list('day_of_week', flat=True))

    context = {
        'doctor': doctor,
        'reviews': reviews,
        'schedules': schedules,
        'slots': slots,
        'today': today,
        'max_date': max_date,
        'selected_date': selected_date,
        'available_days': available_days,
    }
    return render(request, 'pages/doctor_details.html', context)


@login_required
@doctor_required
def doctor_dashboard_view(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-appointment_date', '-start_time')
    todays_appointments = appointments.filter(appointment_date=date.today())
    total_patients = appointments.values('patient').distinct().count()
    avg_review = doctor.reviews.aggregate(Avg('rating'))['rating__avg']
    avg_review = round(avg_review, 1)
    is_available = doctor.is_available
    
    if request.method == 'POST':
        is_available = request.POST.get('is_available') == 'on'
        doctor.is_available = is_available
        doctor.save()
        messages.success(request, "Availability status updated!")
        return redirect(reverse('doctor_dashboard'))

    context = {
        'doctor': doctor,
        'appointments': appointments,
        'todays_appointments': todays_appointments,
        'total_patients': total_patients,
        'avg_review': avg_review,
        "today": date.today(),
        "is_available": is_available,
    }

    return render(request, 'pages/doctor/dashboard.html', context)


@login_required
@doctor_required
def my_patients_view(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    total_patient_count = doctor.appointments.values('patient').distinct().count()
    avg_review = doctor.reviews.aggregate(Avg('rating'))['rating__avg']
    avg_review = round(avg_review, 1)

    patients = Patient.objects.filter(
        appointments__doctor=doctor
    )

    query = request.GET.get('q')
    if query:
        patients = patients.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(id__icontains=query)
        )

    patients = patients.distinct().annotate(
        total_visit=Count('appointments', filter=Q(appointments__doctor=doctor)),
        last_visit=Max('appointments__appointment_date', filter=Q(appointments__doctor=doctor))
    ).order_by('-last_visit')

    paginator = Paginator(patients, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'doctor': doctor,  
        'patients': page_obj,
        'page_obj': page_obj,
        'total_patient_count': total_patient_count,
        'avg_review': avg_review,
        'query': query,
    }
    return render(request, 'pages/doctor/my_patients.html', context)


@login_required
@doctor_required
def doctor_profile_view(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    doctor_form = DoctorProfileForm(instance=doctor)
    password_form = PasswordChangeForm(request.user)

    if request.method == "POST":
        # profile update
        if "update_profile" in request.POST:
            doctor_form = DoctorProfileForm(request.POST, instance=doctor)
            if doctor_form.is_valid():
                doctor_form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('doctor_profile')
            else:
                messages.error(request, "Please correct the error below.")

        # password change
        elif "change_password" in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Password changed successfully")
                return redirect('doctor_profile')
            else:
                messages.error(request, "Please correct the error below.")

    context = {
        'doctor': doctor,
        'doctor_form': doctor_form,
        'password_form': password_form,
    }
    return render(request, 'pages/doctor/doctor_profile.html', context)


@login_required
@doctor_required
def doctor_earning_view(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = doctor.appointments.all().order_by('-appointment_date')
    total_earnings = sum([appointment.payment.amount for appointment in appointments if hasattr(appointment, 'payment') and appointment.payment.status == 'completed'])
    
    this_month_total_earnings = sum([appointment.payment.amount for appointment in appointments if hasattr(appointment, 'payment') and appointment.payment.status == 'completed' and appointment.appointment_date.month == date.today().month and appointment.appointment_date.year == date.today().year])
    this_month_total_earnings_after_fee = sum([appointment.payment.total_amount for appointment in appointments if hasattr(appointment, 'payment') and appointment.payment.status == 'completed' and appointment.appointment_date.month == date.today().month and appointment.appointment_date.year == date.today().year])
    this_month_total_fee = this_month_total_earnings - this_month_total_earnings_after_fee

    current_year = date.today().year
    labels = [month_abbr[i] for i in range(1, 13)] 
    data = []
    for month in range(1, 13):
        month_earnings = sum([
            appointment.payment.amount
            for appointment in appointments
            if hasattr(appointment, 'payment')
            and appointment.payment
            and appointment.payment.status == 'completed'
            and appointment.appointment_date.month == month
            and appointment.appointment_date.year == current_year
        ])
        data.append(float(month_earnings))
    

    context = {
        'doctor': doctor,
        'appointments': appointments,
        'total_earnings': total_earnings,
        'this_month_total_earnings': this_month_total_earnings,
        'this_month_total_earnings_after_fee': this_month_total_earnings_after_fee,
        'this_month_total_fee': this_month_total_fee,
        'labels': labels,
        'data': data,
        'current_year': current_year,
    }
    return render(request, 'pages/doctor/earning.html', context)
