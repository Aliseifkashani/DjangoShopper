from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_direct/', views.login_direct, name='login_direct'),
]