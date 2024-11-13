from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from echos.models import Echo

from .forms import ProfileForm
from .models import Profile


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
    return render(request, 'users/detail.html', {'user': user, 'echos': echos})


@login_required
def my_profile(request):
    username = request.user.username
    return redirect('users:profile', username=username)


@login_required
def edit_profile(request, username):
    user = get_user_model().objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.user != user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        if (form := ProfileForm(request.POST, request.FILES, instance=profile)).is_valid():
            form.save()
            return redirect('users:my-profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile-form.html', dict(form=form))
