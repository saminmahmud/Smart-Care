from django.shortcuts import render, redirect
from doctors.models import Doctor


def index_view(request):
    if request.user.is_authenticated:
        return redirect('redirect_dashboard')
    
    experienced_doctors = Doctor.objects.select_related('user', 'specialization', 'designation').prefetch_related('reviews').order_by('-experience_years')[:4]
    return render(request, "pages/index.html", {'doctors': experienced_doctors})


def services_view(request):
    return render(request, "pages/services.html")


def about_view(request):
    return render(request, "pages/about.html")


def contact_view(request):
    return render(request, "pages/contact.html")


def redirect_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('index')

    if request.user.role == 'patient':
        return redirect('patient_dashboard')

    elif request.user.role == 'doctor':
        return redirect('doctor_dashboard')

    return redirect('index')
