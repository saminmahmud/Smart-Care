from django.urls import path
from .views import medical_report_view, patient_dashboard_view, medical_history_view, patient_profile_view, create_medical_history, create_allergy, create_family_medical_history

urlpatterns = [
    path('patients/dashboard/', patient_dashboard_view, name='patient_dashboard'),
    path('patients/medical-history/', medical_history_view, name='medical_history'),
    path('patients/profile/', patient_profile_view, name='patient_profile'),
    path('patients/medical-reports/', medical_report_view, name='medical_report'),

    path('patients/medical-history/create/', create_medical_history, name='create_medical_history'),
    path('patients/allergy/create/', create_allergy, name='create_allergy'),
    path('patients/family-medical-history/create/', create_family_medical_history, name='create_family_medical_history'),
]
