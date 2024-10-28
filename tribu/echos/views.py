from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
def create_echo(request):
    if request.method == 'POST':
        if (form := EchoForm(request.POST)).is_valid():
            form.save()
            return redirect('echos:echo-list')
    else:
        form = EchoForm()
    return render(request, 'echos/echo-form.html', dict(form=form))


@login_required
def update_echo(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    if request.method == 'POST':
        if (form := EchoForm(request.POST, instance=echo)).is_valid():
            form.save()
            return redirect('echos:echo-list')
    else:
        form = EchoForm(instance=echo)
    return render(request, 'echos/echo-form.html', dict(form=form))
