from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    BLOOD_GROUPS = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, blank=True)
    emergency_contact = models.CharField(max_length=15, blank=True)
    height = models.FloatField(null=True, blank=True)  # in cm
    weight = models.FloatField(null=True, blank=True)  # in kg

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def age(self):
        from datetime import date
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None
    
    @property
    def bmi(self):
        if self.height and self.weight:
            height_in_meters = self.height / 100
            return round(self.weight / (height_in_meters ** 2), 1)
        return None
    
    
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_history')
    condition = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    diagnosis_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.condition}"
    

class FamilyMedicalHistory(models.Model):
    RELATIONSHIP = (
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('sibling', 'Sibling'),
        ('grandparent', 'Grandparent'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='family_medical_history')
    relation = models.CharField(max_length=50, choices=RELATIONSHIP)
    condition = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.relation}: {self.condition}"
    

class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='allergies')
    allergen = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.patient} - Allergy to {self.allergen}"
    

class MedicalReport(models.Model):
    TYPE = (
        ('lab', 'Lab Report'),
        ('imaging', 'Imaging Report'),
        ('prescription', 'Prescription'),
        ('other', 'Other'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_reports')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='medical_reports/')
    description = models.TextField(blank=True)
    report_type = models.CharField(max_length=20, choices=TYPE, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - Report {self.id}"
    