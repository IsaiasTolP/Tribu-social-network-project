from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from echos.models import Echo

from .forms import WaveForm
from .models import Wave


@login_required
def echo_waves(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    waves = Wave.objects.filter(echo=echo)
    return render(
        request,
        'echos/detail.html',
        {
            'echo': echo,
            'waves': waves,
        },
    )


@login_required
def create_wave(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    form = WaveForm(request.POST or None)
    if (form := WaveForm(request.POST)).is_valid():
        wave = form.save(commit=False)
        wave.user = request.user
        wave.echo = echo
        wave.save()
        return redirect('echos:echo-waves', echo_id=echo.id)
    else:
        form = WaveForm()
    return render(request, 'waves/wave-form.html', dict(form=form))


@login_required
def update_wave(request, wave_id):
    wave = Wave.objects.get(id=wave_id)
    echo_id = wave.echo.pk
    if request.user != wave.user:  # Separar del código
        return HttpResponseForbidden()
    form = WaveForm(request.POST or None)
    if (form := WaveForm(request.POST, instance=wave)).is_valid():
        form.save()
        return redirect('echos:echo-waves', echo_id=echo_id)
    else:
        form = WaveForm(instance=wave)
    return render(request, 'waves/wave-form.html', dict(form=form))


@login_required
def delete_wave(request, wave_id):
    wave = Wave.objects.get(id=wave_id)
    if request.user != wave.user:
        return HttpResponseForbidden()
    wave.delete()
    return redirect('echos:echo-list')
