from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from patients.models import Patient
from doctors.models import Doctor, Designation, Specialization

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    # User fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    gender = forms.ChoiceField(choices=User.GENDER, required=False)
    role = forms.ChoiceField(choices=[('patient','Patient'), ('doctor','Doctor')], required=True)

    # Patient extra fields
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    address = forms.CharField(required=False)
    blood_group = forms.ChoiceField(choices=Patient.BLOOD_GROUPS, required=False)
    emergency_contact = forms.CharField(required=False)

    # Doctor extra fields
    designation = forms.ModelChoiceField(queryset=Designation.objects.all(), required=False)
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    consultation_fee = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    hospital_name = forms.CharField(required=False)
    experience_years = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = [
            'email','first_name','last_name','gender','role','password1','password2',
            # Patient fields
            'date_of_birth','address','blood_group','emergency_contact',
            # Doctor fields
            'designation','specialization','bio','consultation_fee','hospital_name','experience_years',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data.get('gender', '')
        user.role = self.cleaned_data['role']
        if commit:
            user.save()

            if user.role == 'doctor':
                Doctor.objects.create(
                    user=user,
                    designation=self.cleaned_data.get('designation'),
                    specialization=self.cleaned_data.get('specialization'),
                    bio=self.cleaned_data.get('bio',''),
                    consultation_fee=self.cleaned_data.get('consultation_fee') or 0,
                    hospital_name=self.cleaned_data.get('hospital_name',''),
                    experience_years=self.cleaned_data.get('experience_years') or 0
                )
            elif user.role == 'patient':
                Patient.objects.create(
                    user=user,
                    date_of_birth=self.cleaned_data.get('date_of_birth'),
                    address=self.cleaned_data.get('address',''),
                    blood_group=self.cleaned_data.get('blood_group',''),
                    emergency_contact=self.cleaned_data.get('emergency_contact','')
                )
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(
        choices=[
            ('patient', 'Patient'),
            ('doctor', 'Doctor'),
            ('admin', 'Admin'),
        ],
        widget=forms.HiddenInput()
    )

    