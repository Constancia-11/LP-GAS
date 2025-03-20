from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ensure 'home' view exists in views.py
]
