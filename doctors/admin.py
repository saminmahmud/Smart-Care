from django.contrib import admin
from .models import Designation, Specialization, Doctor, DoctorSchedule, Review


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DoctorScheduleInline(admin.TabularInline):
    model = DoctorSchedule
    extra = 1


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'specialization', 'hospital_name', 'experience_years')
    search_fields = ('user__first_name', 'user__last_name', 'hospital_name')
    list_filter = ('designation', 'specialization')
    inlines = [DoctorScheduleInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'rating', 'created_at')
    search_fields = ('doctor__user__first_name', 'doctor__user__last_name', 'patient__first_name', 'patient__last_name')
    list_filter = ('rating', 'created_at')
