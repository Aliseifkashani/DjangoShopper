from django.urls import path

from . import views

app_name = 'log'

urlpatterns = [
    path('in_direct/', views.direct, name='direct'),
    path('in_indirect/', views.indirect, name='indirect'),
    path('out/', views.logout, name='logout'),
    path('test/', views.test),
]
