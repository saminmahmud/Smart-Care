from django.contrib import admin
from django.urls import include, path
from smart_care.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index_view, name='index'),
    path('services/', services_view, name='services'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('redirect-dashboard/', redirect_dashboard, name='redirect_dashboard'),
    
    path('', include('accounts.urls')),
    path('', include('doctors.urls')),
    path('', include('patients.urls')),
    path('', include('appointments.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]


# Only used in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)