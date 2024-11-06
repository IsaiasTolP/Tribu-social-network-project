from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('<username>/', views.profile, name='profile'),
]