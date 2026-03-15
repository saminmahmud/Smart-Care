from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import models
from accounts.decorators import patient_required
from appointments.models import Medication
from patients.forms import CreateAllergyForm, CreateFamilyMedicalHistoryForm, CreateMedicalHistoryForm
from patients.models import Patient


@login_required
@patient_required
def patient_dashboard_view(request):
    patient = Patient.objects.select_related('user').get(user=request.user)
    appointments = patient.appointments.select_related('doctor__user').order_by('-appointment_date')
    scheduled_apointments_count = appointments.filter(status='scheduled').count()
    completed_apointments_count = appointments.filter(status='completed').count()
    active_prescriptions_count = patient.prescriptions.filter(is_active=True).count()
    total_spent = appointments.aggregate(total=models.Sum('payment__amount'))['total'] or 0
    active_medications = Medication.objects.filter(prescription__patient=patient, is_active=True).select_related('prescription__doctor__user')[:5]
    medical_histories = patient.medical_history.order_by('-diagnosis_date')[:3]

    context = {
        'patient': patient,
        'appointments': appointments[:3],
        'scheduled_appointments_count': scheduled_apointments_count,
        'completed_appointments_count': completed_apointments_count,
        'active_prescriptions_count': active_prescriptions_count,
        'total_spent': total_spent,
        'active_medications': active_medications,
        'medical_histories': medical_histories,
    }
    return render(request, "pages/patient/dashboard.html", context)


@login_required
@patient_required
def medical_history_view(request):
    patient = Patient.objects.select_related('user').get(user=request.user)
    medical_histories = patient.medical_history.order_by('-diagnosis_date')
    family_medical_histories = patient.family_medical_history.all()
    allergies = patient.allergies.all()

    context = {
        'patient': patient,
        'medical_histories': medical_histories,
        'family_medical_histories': family_medical_histories,
        'allergies': allergies,
    }
    return render(request, "pages/patient/medical_history.html", context)


@login_required
@patient_required
def patient_profile_view(request):
    patient = Patient.objects.select_related('user').get(user=request.user)
    context = {
        'patient': patient,
    }
    return render(request, "pages/patient/patient_profile.html", context)


def medical_report_view(request):
    patient = Patient.objects.select_related('user').get(user=request.user)
    medical_reports = patient.medical_reports.order_by('-upload_date')
    context = {
        'medical_reports': medical_reports,
    }
    return render(request, "pages/patient/medical_report.html", context)


@login_required
@patient_required
def create_medical_history(request):
    if request.method == "POST":
        form = CreateMedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_history = form.save(commit=False)
            medical_history.patient = request.user.patient
            medical_history.save()
            return redirect('medical_history')
    else:
        form = CreateMedicalHistoryForm()
    context = {
        'form': form,
    }
    return render(request, "pages/patient/create_medical_history.html", context)


@login_required
@patient_required
def create_allergy(request):
    if request.method == "POST":
        form = CreateAllergyForm(request.POST)
        if form.is_valid():
            allergy = form.save(commit=False)
            allergy.patient = request.user.patient
            allergy.save()
            return redirect('medical_history')
    else:
        form = CreateAllergyForm()
    context = {
        'form': form,
    }
    return render(request, "pages/patient/create_allergy.html", context)


@login_required
@patient_required
def create_family_medical_history(request):
    if request.method == "POST":
        form = CreateFamilyMedicalHistoryForm(request.POST)
        if form.is_valid():
            family_history = form.save(commit=False)
            family_history.patient = request.user.patient
            family_history.save()
            return redirect('medical_history')
    else:
        form = CreateFamilyMedicalHistoryForm()
    context = {
        'form': form,
    }
    return render(request, "pages/patient/create_family_medical_history.html", context)







