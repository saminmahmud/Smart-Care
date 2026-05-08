from django.contrib import admin
from .models import Appointment, Payment, Prescription, Medication, PlatformFee


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'start_time', 'end_time', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('appointment__patient__first_name', 'appointment__patient__last_name', 'appointment__doctor__first_name', 'appointment__doctor__last_name')


class MedicationInline(admin.TabularInline):
    model = Medication
    extra = 1


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    inlines = [MedicationInline]


@admin.register(PlatformFee)
class PlatformFeeAdmin(admin.ModelAdmin):
    list_display = ('fee_percentage', 'updated_at')
    list_filter = ('updated_at',)
