from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import models
from accounts.decorators import doctor_required, patient_required
from appointments.models import Appointment, Medication
from patients.forms import CreateAllergyForm, CreateFamilyMedicalHistoryForm, CreateMedicalHistoryForm, PatientProfileForm
from patients.models import Patient
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



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


@login_required
@patient_required
def patient_profile_view(request):
    patient = Patient.objects.select_related('user').get(user=request.user)
    patient_form = PatientProfileForm(instance=patient)
    password_form = PasswordChangeForm(request.user)

    if request.method == "POST":
        # profile update
        if "update_profile" in request.POST:
            patient_form = PatientProfileForm(request.POST, instance=patient)
            if patient_form.is_valid():
                patient_form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('patient_profile')
            else:
                messages.error(request, "Please correct the error below.")

        # password change
        elif "change_password" in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Password changed successfully")
                return redirect('patient_profile')
            else:
                messages.error(request, "Please correct the error below.")
            
    context = {
        'patient': patient,
        'patient_form': patient_form,
        'password_form': password_form,
    }
    return render(request, "pages/patient/patient_profile.html", context)



@login_required
@doctor_required
def patient_profile_for_doctor_view(request, patient_id):
    patient = Patient.objects.select_related('user').get(id=patient_id)
    doctor = request.user.doctor
    allergies = patient.allergies.all()
    medical_histories = patient.medical_history.order_by('-diagnosis_date')
    total_visit = patient.appointments.filter(patient=patient, doctor=doctor).count()
    review = doctor.reviews.filter(patient=patient).first()
    current_conditions = patient.medical_history.filter(is_active=True).order_by('-diagnosis_date')
    medical_reports = patient.medical_reports.order_by('-upload_date')
     
    context = {
        'patient': patient,
        'doctor': doctor,
        'allergies': allergies,
        'medical_histories': medical_histories,
        'total_visit': total_visit,
        'rating': review.rating if review else 'N/A',
        'current_conditions': current_conditions,
        'medical_reports': medical_reports,
    }
    return render(request, "pages/doctor/patient_profile.html", context)


