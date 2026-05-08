from django.urls import path
from .views import *

urlpatterns = [
    path('patient/my-appointments/', my_appointments, name='my_appointments'),
    path('patient/appointment/<int:appointment_id>/', appointment_details_view, name='appointment_detail'),
    path('patient/my-prescriptions/', my_prescriptions_view, name='my_prescription'),
    path('patient/payment-history/', payment_history_view, name='payment_history'),
    path('patient/prescription/<int:id>/', prescription_detail_view, name="prescription_detail"),

    path('doctor/appointments/', appointments, name='doctor_appointments'),
    path('doctor/write-prescription/<int:appointment_id>/<int:patient_id>/', write_prescription_view, name='write_prescription'),
    path('doctor/write-prescription/<int:appointment_id>/<int:patient_id>/edit/<int:prescription_id>/', write_prescription_view, name='edit_prescription'),
    path('doctor/update-appointment-status/<int:appointment_id>/', update_appointment_status, name='update_appointment_status'),

    path('video-call/<int:appointment_id>/', video_call, name='video_call'),
]
