from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('login_direct/', views.login_direct, name='login_direct'),
    path('logout/', views.logout, name='logout'),
]
