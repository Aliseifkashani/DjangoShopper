from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:userID>/profile/', views.profile, name='profile'),
    path('<int:userID>/update/', views.update, name='update'),
]
