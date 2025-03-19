from django.db import models
from users.models import CustomUser

class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audit log by {self.user.username} at {self.timestamp}"

