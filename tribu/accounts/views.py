from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignupForm

"""
def user_login(request):
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['passsword']
            if user := authenticate(request, username, password):
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'login.html', dict(form=form))
"""


def user_signup(request):
    form = SignupForm(request.POST or None)
    if (form := SignupForm(request.POST)).is_valid():
        user = form.save()
        login(request, user)
        return redirect('echos:echo-list')
    return render(request, 'registration/signup.html', dict(form=form))


def successful_logout(request):
    if request.user.is_authenticated:
        return redirect('logout')
    return render(request, 'registration/logout.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
