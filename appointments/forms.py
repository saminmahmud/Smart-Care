from django import forms
from django.forms import inlineformset_factory
from .models import Prescription, Medication


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = [
            'diagnosis',
            'note',
        ]

        widgets = {
            'diagnosis': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter diagnosis'
            }),
            'note': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Additional notes'
            }),
        }


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = [
            'name',
            'dosage',
            'frequency',
            'duration',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Medicine name'
            }),
            'dosage': forms.TextInput(attrs={
                'placeholder': 'Dosage'
            }),
            'frequency': forms.TextInput(attrs={
                'placeholder': 'Frequency'
            }),
            'duration': forms.TextInput(attrs={
                'placeholder': 'Duration'
            }),
        }


MedicationFormSet = inlineformset_factory(
    Prescription,
    Medication,
    form=MedicationForm,
    extra=0,
    can_delete=True
)


class SymptomCheckerForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "e.g. I have chest pain for 2 days, shortness of breath, and dizziness...",
            "rows": 1,
            "required": True
        })
    )