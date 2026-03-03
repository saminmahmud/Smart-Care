from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
     
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    bio = models.TextField(blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hospital_name = models.CharField(max_length=255, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(help_text="Duration of each appointment slot in minutes")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} - {self.day_of_week} ({self.start_time} - {self.end_time})"
    

class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.doctor} by {self.patient}"
    

