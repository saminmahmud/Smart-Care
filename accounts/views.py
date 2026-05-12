from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import patient_required
from accounts.forms import UserRegisterForm, UserLoginForm
from patients.models import Patient


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid registration details.")
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            role = form.cleaned_data.get("role")

            if user.role != role:
                messages.error(request, "Invalid role selected.")
                return redirect("login")
            
            login(request, user)
            messages.success(request, "Login successful!")

            return redirect('redirect_dashboard')
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'pages/login.html', {'form': form})
           

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
