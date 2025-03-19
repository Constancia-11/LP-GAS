from django.db import models

from django.db import models
from outlets.models import Outlet

class Stock(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    available_cylinders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.outlet.name} - {self.available_cylinders} cylinders"

