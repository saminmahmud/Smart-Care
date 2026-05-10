from django.urls import path
from .views import *

urlpatterns = [
    path('doctors/', doctors_list_view, name='doctors_list'),
    path('doctors/<int:doctor_id>/', doctor_details_view, name='doctor_details'),
    path('doctors/<int:doctor_id>/reviews/create/', create_review_view, name='create_review'),
    path('doctors/dashboard/', doctor_dashboard_view, name='doctor_dashboard'),
    path('doctors/my-patients/', my_patients_view, name='my_patients'),
    path('doctor/profile/', doctor_profile_view, name='doctor_profile'),
    path('doctor/earnings/', doctor_earning_view, name='doctor_earnings'),
]
