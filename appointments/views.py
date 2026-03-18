from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from accounts.decorators import patient_required
from appointments.models import Appointment, Prescription
from django.db import models
from patients.models import Patient
from django.core.paginator import Paginator 


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
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user.patient)
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