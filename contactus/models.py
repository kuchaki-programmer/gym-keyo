from account.models import CustomUser
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()

    def __str__(self):
        return self.message[:15]
