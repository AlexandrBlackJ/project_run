from django.db import models
from django.contrib.auth.models import User


class Run(models.Model):
    """Модель для сбора данных с забегов"""
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
