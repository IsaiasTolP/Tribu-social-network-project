from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('@me/', views.my_profile, name='my-profile'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/echos/', views.user_echo_list, name='user-echo-list'),
]
