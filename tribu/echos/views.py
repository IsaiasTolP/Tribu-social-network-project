from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from waves.models import Wave

from .forms import EchoForm
from .models import Echo


@login_required
def echo_list(request):
    echos = Echo.objects.all()
    return render(
        request,
        'echos/home.html',
        {
            'echos': echos,
        },
    )


@login_required
def echo_detail(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    waves = Wave.objects.filter(echo=echo)[:5]
    return render(
        request,
        'echos/detail.html',
        {
            'echo': echo,
            'waves': waves,
        },
    )


@login_required
def create_echo(request):
    form = EchoForm(request.POST or None)
    if (form := EchoForm(request.POST)).is_valid():
        echo = form.save(commit=False)
        echo.user = request.user
        echo.save()
        return redirect('echos:echo-list')
    else:
        form = EchoForm()
    return render(request, 'echos/echo-form.html', dict(form=form))


@login_required
def update_echo(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    if request.user != echo.user:
        return HttpResponseForbidden()
    form = EchoForm(request.POST or None)
    if (form := EchoForm(request.POST, instance=echo)).is_valid():
        form.save()
        return redirect('echos:echo-list')
    else:
        form = EchoForm(instance=echo)
    return render(request, 'echos/echo-form.html', dict(form=form))


@login_required
def delete_echo(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    if request.user != echo.user:
        return HttpResponseForbidden()
    echo.delete()
    return redirect('echos:echo-list')
