from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from appointments.models import Appointment
from doctors.models import Doctor, DoctorSchedule, Review, Specialization
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from django.contrib import messages
from doctors.utils import get_daily_slots
from patients.models import Patient



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

    # Rating filter — avg rating দিয়ে filter
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

    # Query params from pagination এ use করার জন্য (page বাদ দিয়ে)
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
        'query_params': query_params.urlencode(),  # urlencode করা
    }

    return render(request, 'pages/doctor.html', context)


def doctor_details_view(request, doctor_id):

    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, id=doctor_id)
        patient = request.user.patient
        # patient = Patient.objects.first() 

        slot_str = request.POST.get("selected_slot")
        appointment_date_str = request.POST.get("selected_date")

        if not slot_str or not appointment_date_str:
            messages.error(request, "Please select a date and time slot.")
            return redirect('doctor_details', doctor_id=doctor.id)

        start_time = datetime.strptime(slot_str, "%H:%M").time()
        appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d").date()

        if appointment_date < date.today() or appointment_date > date.today() + timedelta(days=7):
            messages.error(request, "You can only book within the next 7 days!")
            return redirect('doctor_details', doctor_id=doctor.id)

        if Appointment.objects.filter(doctor=doctor, appointment_date=appointment_date, start_time=start_time, status='scheduled').exists():
            messages.error(request, "Sorry, this slot is already booked!")
            return redirect('doctor_details', doctor_id=doctor.id)

        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            start_time=start_time,
            end_time=(datetime.combine(appointment_date, start_time) + doctor.schedules.filter(is_active=True).first().slot_duration * timedelta(minutes=1)).time() 
        )
        # print("Creating appointment with:", doctor, patient, appointment_date, start_time)

        messages.success(request, "Appointment booked successfully!")
        return redirect('doctor_details', doctor_id=doctor.id)

    doctor = Doctor.objects.select_related('user', 'specialization', 'designation').prefetch_related('reviews').get(id=doctor_id)
    reviews = doctor.reviews.all()
    schedules = DoctorSchedule.objects.filter(doctor=doctor, is_active=True)
    today = date.today()
    max_date = today + timedelta(days=7)

    slots = get_daily_slots(doctor, today)

    context = {
        'doctor': doctor,
        'reviews': reviews,
        'schedules': schedules,
        'slots': slots,
        'today': today,
        'max_date': max_date,
    }

    return render(request, 'pages/doctor_details.html', context)


