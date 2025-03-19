from django.db import models

class Outlet(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
