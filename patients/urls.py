from django.urls import path
from .views import *
urlpatterns = [
    path('patients/dashboard/', patient_dashboard_view, name='patient_dashboard'),
    path('patients/medical-history/', medical_history_view, name='medical_history'),
    path('patients/profile/', patient_profile_view, name='patient_profile'),
    path('patients/medical-reports/', medical_report_view, name='medical_report'),
    path('patients/medical-reports/create/', create_medical_report, name='create_medical_report'),
    path('patients/medical-reports/<int:report_id>/', medical_report_detail_view, name='medical_report_detail'),
    path('patients/medical-reports/<int:report_id>/delete/', delete_report, name='delete_report'),
    path('patients/medical-history/create/', create_medical_history, name='create_medical_history'),
    path('patients/allergy/create/', create_allergy, name='create_allergy'),
    path('patients/family-medical-history/create/', create_family_medical_history, name='create_family_medical_history'),
    path('patients/<int:patient_id>/profile/', patient_profile_for_doctor_view, name='patient_profile_for_doctor'),
]
