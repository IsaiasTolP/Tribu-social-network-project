from django import forms

from .models import Echo


class EchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
