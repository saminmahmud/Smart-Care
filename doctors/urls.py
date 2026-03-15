from django.urls import path
from .views import doctors_list_view, doctor_details_view

urlpatterns = [
    path('doctors/', doctors_list_view, name='doctors_list'),
    path('doctors/<int:doctor_id>/', doctor_details_view, name='doctor_details'),
]
