from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from echos.models import Echo

from .models import Wave


@login_required
def echo_waves(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    waves = Wave.objects.get(echo=echo)
    return render(
        request,
        'waves/echo-waves.html',
        {'waves': waves},
    )


@login_required
def create_wave(request):
    pass
