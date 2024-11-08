from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from echos.models import Echo


@login_required
def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'users/users.html', {'users': users})


@login_required
def profile(request, username):
    user = get_user_model().objects.get(username=username)
    echos = Echo.objects.filter(user=user)[:5]
    return render(request, 'users/profile.html', {'user': user, 'echos': echos})


@login_required
def user_echo_list(request, username):
    user = get_user_model().objects.get(username=username)
    echos = Echo.objects.filter(user=user)
    return render(request, 'users/profile.html', {'user': user, 'echos': echos})
