from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.create_echo, name='create-echo'),
    path('<id>/edit/', views.update_echo, name='update-echo'),
]
