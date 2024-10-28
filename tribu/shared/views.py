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
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'registration/signup.html', dict(form=form))


def user_list(request):
    pass


def profile(request):
    pass
