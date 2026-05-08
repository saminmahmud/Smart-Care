from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.decorators import doctor_required, patient_required
from appointments.forms import PrescriptionForm
from appointments.forms import MedicationFormSet
from appointments.models import Appointment, Prescription
from django.db import models
from patients.models import Patient
from django.core.paginator import Paginator 
from django.contrib import messages
from smart_care.settings import ServerSecret, AppID


@login_required
@patient_required
def my_appointments(request):
    filter_status = request.GET.get('status', 'all')
    patient = request.user.patient

    if filter_status == 'scheduled':
        appointments = patient.appointments.filter(status='scheduled').select_related('doctor__user').prefetch_related('prescriptions').order_by('-appointment_date')
    elif filter_status == 'completed':
        appointments = patient.appointments.filter(status='completed').select_related('doctor__user').prefetch_related('prescriptions').order_by('-appointment_date')
    elif filter_status == 'canceled':
        appointments = patient.appointments.filter(status='canceled').select_related('doctor__user').prefetch_related('prescriptions').order_by('-appointment_date')
    else:
        filter_status = 'all'
        appointments = patient.appointments.all().select_related('doctor__user').prefetch_related('prescriptions').order_by('-appointment_date')

    schedule_appointment_count = patient.appointments.filter(status='scheduled').count()
    completed_appointment_count = patient.appointments.filter(status='completed').count()
    canceled_appointment_count = patient.appointments.filter(status='canceled').count()
    total_appointment_count = patient.appointments.count()

    context = {
        'patient': patient,
        'appointments': appointments,
        'filter_status': filter_status,
        'schedule_appointment_count': schedule_appointment_count,
        'completed_appointment_count': completed_appointment_count,
        'canceled_appointment_count': canceled_appointment_count,
        'total_appointment_count': total_appointment_count,
    }

    return render(request, 'pages/patient/my_appointments.html', context)


def appointment_details_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    context = {
        'appointment': appointment,
    }
    return render(request, 'pages/patient/appointment_detail.html', context)


@login_required
@patient_required
def my_prescriptions_view(request):
    filter_status = request.GET.get('status', 'all')
    patient = request.user.patient
    active_prescriptions = patient.prescriptions.filter(is_active=True).count()
    expired_prescriptions = patient.prescriptions.filter(is_active=False).count()
    if filter_status == 'active':
        prescriptions = patient.prescriptions.filter(is_active=True).select_related('doctor__user').order_by('-created_at')
    elif filter_status == 'expired':
        prescriptions = patient.prescriptions.filter(is_active=False).select_related('doctor__user').order_by('-created_at')
    else:
        filter_status = 'all'
        prescriptions = patient.prescriptions.all().select_related('doctor__user').order_by('-created_at')

    context = {
        'patient': patient,
        'prescriptions': prescriptions,
        'active_prescriptions': active_prescriptions,
        'expired_prescriptions': expired_prescriptions,
        'filter_status': filter_status,
    }
    return render(request, 'pages/patient/my_prescriptions.html', context)


@login_required
@patient_required
def prescription_detail_view(request, id):
    patient = request.user.patient
    prescription = Prescription.objects.select_related('doctor__user').get(id=id, patient=request.user.patient)
    context = {
        'patient': patient,
        'prescription': prescription,
    }
    return render(request, "pages/patient/prescription_detail.html", context)


@login_required
@patient_required
def payment_history_view(request):
    filter_status = request.GET.get('status', 'all')
    patient = request.user.patient

    payments = patient.appointments.filter(payment__isnull=False).select_related('payment').order_by('-appointment_date')
    total_spent = payments.aggregate(total=models.Sum('payment__amount'))['total'] or 0
    total_completed_payments = payments.filter(payment__status='completed').count()

    if filter_status == 'completed':
        payments = payments.filter(payment__status='completed')
    elif filter_status == 'failed':
        payments = payments.filter(payment__status='failed')
    
    payments = payments.distinct()


    # Pagination
    paginator = Paginator(payments, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Query params from pagination
    query_params = request.GET.copy()
    query_params.pop('page', None)

    context = {
        'patient': patient,
        'payments': payments,
        'total_spent': total_spent,
        'total_completed_payments': total_completed_payments,
        'filter_status': filter_status,
        'page_obj': page_obj,
        'query_params': query_params.urlencode(),
    }
    return render(request, 'pages/patient/payment_history.html', context)


# Doctor

@login_required
@doctor_required
def appointments(request):
    filter_status = request.GET.get('status', 'all')
    doctor = request.user.doctor

    if filter_status == 'scheduled':
        appointments = doctor.appointments.filter(status='scheduled').select_related('patient__user', 'prescriptions').order_by('-appointment_date')
    elif filter_status == 'completed':
        appointments = doctor.appointments.filter(status='completed').select_related('patient__user', 'prescriptions').order_by('-appointment_date')
    elif filter_status == 'canceled':
        appointments = doctor.appointments.filter(status='canceled').select_related('patient__user', 'prescriptions').order_by('-appointment_date')
    else:
        filter_status = 'all'
        appointments = doctor.appointments.all().select_related('patient__user', 'prescriptions').order_by('-appointment_date')

    schedule_appointment_count = doctor.appointments.filter(status='scheduled').count()
    completed_appointment_count = doctor.appointments.filter(status='completed').count()
    canceled_appointment_count = doctor.appointments.filter(status='canceled').count()
    total_appointment_count = doctor.appointments.count()

    context = {
        'doctor': doctor,
        'appointments': appointments,
        'filter_status': filter_status,
        'schedule_appointment_count': schedule_appointment_count,
        'completed_appointment_count': completed_appointment_count,
        'canceled_appointment_count': canceled_appointment_count,
        'total_appointment_count': total_appointment_count,
    }

    return render(request, 'pages/doctor/appointments.html', context)


@login_required
@doctor_required
def write_prescription_view(request, appointment_id, patient_id, prescription_id=None):
    doctor = request.user.doctor
    patient = get_object_or_404(Patient, id=patient_id)
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor, patient=patient)

    if prescription_id:
        prescription = get_object_or_404(Prescription, id=prescription_id, appointment=appointment)
    else:
        prescription = Prescription.objects.filter(appointment=appointment).first()

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)

        if form.is_valid():
            rx = form.save(commit=False)
            rx.doctor = doctor
            rx.patient = patient
            rx.appointment = appointment
            rx.save()

            formset = MedicationFormSet(request.POST, instance=rx)
            if formset.is_valid():
                formset.save()
                return redirect('edit_prescription', appointment_id=appointment_id, patient_id=patient_id, prescription_id=rx.id)
        else:
            formset = MedicationFormSet(request.POST, instance=prescription)

    else:
        form = PrescriptionForm(instance=prescription)
        formset = MedicationFormSet(instance=prescription)

    context = {
        'doctor': doctor,
        'patient': patient,
        'appointment': appointment,
        'form': form,
        'formset': formset,
        'prescription': prescription,
    }
    return render(request, 'pages/doctor/write_prescription.html', context)


@login_required
def video_call(request, appointment_id):

    appointment = get_object_or_404(Appointment, id=appointment_id)

    # appointment day check
    today = timezone.localdate()

    if appointment.appointment_date.date() != today:
        if request.user.role == 'doctor':
            messages.error(request, "You can only start the video call on the day/time of the appointment.")
            return redirect('doctor_appointments')
        else:
            messages.error(request, "You can only join the video call on the day/time of the appointment.")
            return redirect('my_appointments')

    context = {
        'appointment': appointment,
        'room_id': appointment.meeting_name,
        'app_id': AppID,
        'server_secret': ServerSecret,
    }

    return render(request, 'pages/video_call.html', context)


@login_required
@doctor_required
def update_appointment_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user.doctor)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Appointment.STATUS_CHOICES).keys():
            appointment.status = new_status
            appointment.save()
            messages.success(request, "Appointment status updated successfully.")
            return redirect('doctor_appointments')

    return redirect('doctor_appointments')