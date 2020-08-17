from django.urls import path

from . import views

app_name = 'prof'

urlpatterns = [
    path('profile/', views.profile, name='prof'),
    path('update/', views.update, name='update'),
]
