from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from smart_care.views import contact_view, index_view, redirect_dashboard, services_view, about_view, custom_404
from django.conf.urls import handler404


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
    
    # path('err/', custom_404, name='custom_404'),
]

handler404 = custom_404


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

