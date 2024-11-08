from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('<wave_id>/edit/', views.update_wave, name='update-wave'),
    path('<wave_id>/delete/', views.delete_wave, name='delete-wave'),
]
