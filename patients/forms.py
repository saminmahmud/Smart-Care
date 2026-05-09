from django import forms
from .models import MedicalReport, Patient, MedicalHistory, FamilyMedicalHistory, Allergy

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


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "height",
            "weight",
            "address",
            "emergency_contact",
        ]
        widgets = {
            "height": forms.NumberInput(attrs={
                'placeholder': 'Enter height in cm'
            }),
            "weight": forms.NumberInput(attrs={
                'placeholder': 'Enter weight in kg'
            }),
            "address": forms.TextInput(attrs={
                'placeholder': 'Enter address'
            }),
            "emergency_contact": forms.TextInput(attrs={
                'placeholder': 'Enter emergency contact number',
            }),
        }

    def clean_emergency_contact(self):
        contact = self.cleaned_data.get('emergency_contact')
        if contact and not contact.isdigit():
            raise forms.ValidationError("Emergency contact must contain only digits.")
        return contact
    
    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height <= 0:
            raise forms.ValidationError("Height must be a positive number.")
        return height
    
    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight


class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['title', 'file', 'description', 'report_type']
        labels = {
            'title': 'Title',
            'file': 'File',
            'description': 'Description',
            'report_type': 'Report Type'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter report title'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write details about the report'
            }),
            'report_type': forms.Select(attrs={
                'placeholder': 'Select report type'
            }),
        }  