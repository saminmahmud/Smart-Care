from django import forms
from .models import Patient, MedicalHistory, FamilyMedicalHistory, Allergy

class CreateMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['condition', 'description', 'diagnosis_date']
        labels = {
            'condition': 'Medical Condition',
            'description': 'Description',
            'diagnosis_date': 'Diagnosis Date',
        }
        widgets = {
            'condition': forms.TextInput(attrs={
                'placeholder': 'Enter medical condition'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write details about the condition'
            }),
            'diagnosis_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }


class CreateAllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ['allergen',]
        labels = {
            'allergen': 'Allergen',
        }
        widgets = {
            'allergen': forms.TextInput(attrs={
                'placeholder': 'Enter allergen'
            }),
        }


class CreateFamilyMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = FamilyMedicalHistory
        fields = ['relation', 'condition', 'description']
        labels = {
            'relation': 'Relation',
            'condition': 'Medical Condition',
            'description': 'Description',
        }
        widgets = {
            'relation': forms.Select(attrs={
                'placeholder': 'Select relation'
            }),
            'condition': forms.TextInput(attrs={
                'placeholder': 'Enter medical condition'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write details about the condition'
            }),
        }