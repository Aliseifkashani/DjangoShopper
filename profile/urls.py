from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path('<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/update/', views.update, name='update'),
]
