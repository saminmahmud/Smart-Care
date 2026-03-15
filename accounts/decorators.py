from django.http import HttpResponseForbidden

def patient_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'patient':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view

def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'doctor':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view