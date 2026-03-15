from django.contrib import admin
from .models import Patient, MedicalHistory, MedicalReport, FamilyMedicalHistory, Allergy

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'blood_group')
    search_fields = ('user__first_name', 'user__last_name', 'blood_group')
    list_filter = ('blood_group',)


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'condition', 'diagnosis_date')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'condition')
    list_filter = ('diagnosis_date',)


@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'title', 'report_type', 'upload_date')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'title')
    list_filter = ('report_type', 'upload_date')


@admin.register(FamilyMedicalHistory)
class FamilyMedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'relation', 'condition')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'condition')
    list_filter = ('relation',)


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('patient', 'allergen')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'allergen')