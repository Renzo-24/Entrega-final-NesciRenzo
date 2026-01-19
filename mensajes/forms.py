from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all(), label="Para")

    class Meta:
        model = Mensaje
        fields = ['receptor', 'asunto', 'cuerpo']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

