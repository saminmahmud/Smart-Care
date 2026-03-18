from django.urls import path
from .views import appointment_details_view, my_appointments, my_prescriptions_view, payment_history_view, prescription_detail_view

urlpatterns = [
    path('patient/my-appointments/', my_appointments, name='my_appointments'),
    path('patient/appointment/<int:appointment_id>/', appointment_details_view, name='appointment_detail'),
    path('patient/my-prescriptions/', my_prescriptions_view, name='my_prescription'),
    path('patient/payment-history/', payment_history_view, name='payment_history'),
    path('patient/prescription/<int:id>/', prescription_detail_view, name="prescription_detail")
]
