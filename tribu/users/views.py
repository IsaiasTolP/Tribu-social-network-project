from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'users/users.html', {'users': users})


@login_required
def profile(request, username):
    user = get_user_model().objects.get(username=username)
    return render(request, 'users/profile.html', {'user': user})
