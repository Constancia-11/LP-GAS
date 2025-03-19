from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('manager', 'Outlet Manager'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    nic = models.CharField(max_length=12, unique=True, null=True, blank=True)  # National ID Card
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"