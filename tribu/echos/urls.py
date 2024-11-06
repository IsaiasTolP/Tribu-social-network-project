from django.urls import path

from waves import views as wave_views

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.create_echo, name='create-echo'),
    path('<echo_id>/', views.echo_detail, name='echo-detail'),
    path('<echo_id>/edit/', views.update_echo, name='update-echo'),
    path('<echo_id>/delete/', views.delete_echo, name='delete-echo'),
    path('<echo_id>/waves/', views.echo_waves, name='echo-waves'),
    path('<echo_id>/waves/add/', wave_views.create_wave, name='create-wave'),
]
