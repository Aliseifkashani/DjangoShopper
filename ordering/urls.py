from django.urls import path

from . import views
from .tests import CommidityModelTests


urlpatterns = [
    path('view/', views.view_products, name='view_products'),
    path('buy/', views.buy, name='buy'),
]
