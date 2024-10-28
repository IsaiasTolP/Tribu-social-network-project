from django.contrib import admin

from .models import Echo


@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = ('content',)
