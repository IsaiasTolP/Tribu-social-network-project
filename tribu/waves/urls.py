from django.urls import path

from . import views

app_name = 'waves'
urlpatterns = [
    path('', views.echo_waves, name='echo-waves'),
    path('add/', views.create_wave, name='create-wave'),
]