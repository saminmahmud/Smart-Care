from django.db import models
from accounts.managers import CustomUserManager
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    ROLE = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True, validators=[EmailValidator()])
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    role = models.CharField(max_length=10, choices=ROLE, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


