from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('log.urls')),
    path('prof/', include('prof.urls')),
    path('ordering/', include('ordering.urls')),
]
