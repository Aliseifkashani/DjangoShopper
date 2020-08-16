from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('log.urls')),
    path('prof/', include('prof.urls')),
    path('ordering/', include('ordering.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('logout/', views.logout),
]
