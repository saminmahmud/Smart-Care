from django import forms
from .models import Doctor


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['designation', 'specialization', 'bio', 'consultation_fee', 'hospital_name', 'experience_years', 'is_available']
        widgets = {
            'designation': forms.Select(attrs={
                'placeholder': 'Select designation'
            }),
            'specialization': forms.Select(attrs={
                'placeholder': 'Select specialization'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write a brief biography about yourself'
            }),
            'consultation_fee': forms.NumberInput(attrs={
                'placeholder': 'Enter consultation fee'
            }),
            'hospital_name': forms.TextInput(attrs={
                'placeholder': 'Enter hospital name'
            }),
            'experience_years': forms.NumberInput(attrs={
                'placeholder': 'Enter years of experience'
            }),
        }