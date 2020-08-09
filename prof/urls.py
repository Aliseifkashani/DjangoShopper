from django.urls import path

from . import views

app_name = 'prof'

urlpatterns = [
    path('<int:user_id>/', views.profile, name='prof'),
    path('<int:user_id>/update/', views.update, name='update'),
]
