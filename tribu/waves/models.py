from django.contrib.auth.models import User
from django.db import models


class Wave(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    echo = models.ForeignKey(
        'echos.Echo',
        related_name='echos',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
