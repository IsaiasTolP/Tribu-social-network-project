from django.conf import settings
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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-created_at']
