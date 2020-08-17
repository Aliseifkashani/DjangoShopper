from django.urls import path

from . import views

app_name = 'log'

urlpatterns = [
    path('in/', views.direct, name='direct'),
    path('out/', views.logout, name='logout'),
    path('test/', views.test),
]
