from django.urls import path
from .views import login_view, register_view

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),

]
