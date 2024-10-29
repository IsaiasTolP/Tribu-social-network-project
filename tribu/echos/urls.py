from django.urls import include, path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.create_echo, name='create-echo'),
    path('<echo_id>/', views.echo_detail, name='echo-detail'),
    path('<echo_id>/edit/', views.update_echo, name='update-echo'),
    path('<echo_id>/waves/', include('waves.urls')),
]
