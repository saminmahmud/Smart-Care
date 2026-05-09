import uuid
from django.db import models
from doctors.models import Doctor
from django.contrib.auth import get_user_model
from patients.models import Patient

User = get_user_model()


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    meeting_name = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.id} - Dr. {self.doctor.user.first_name} {self.doctor.user.last_name} with {self.patient.user.first_name} {self.patient.user.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.meeting_name:
            self.meeting_name = f"Appointment_{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['doctor', 'appointment_date', 'start_time']


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions')
    appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions')
    diagnosis = models.TextField(blank=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor} - {self.is_active}"
    

class Medication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} for {self.prescription.patient}"
    

class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    stripe_session_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment for {self.appointment} - Status: {self.status}"
    
    @property
    def platform_fee(self):
        fee = PlatformFee.objects.first()
        if fee:
            return round((self.amount * fee.fee_percentage) / 100, 2)
        return 0
    
    @property
    def total_amount(self):
        return round(self.amount - self.platform_fee, 2)
    
    
class PlatformFee(models.Model):
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Platform Fee: {self.fee_percentage}%"
    