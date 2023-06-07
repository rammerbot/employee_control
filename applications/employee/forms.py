from django import forms

from .models import *


class CheckForm(forms.Form):

    CHOICES=(
        ('El Viejo','El Viejo'),
        ('Sport','Sport'),
        ('Km - 40','Km - 40'),
        ('Veterinaria San Pedro', 'Veterinaria San Pedro'),
    )

    branch = forms.ChoiceField(label='Sucursal', choices=CHOICES, required=True)
    card = forms.CharField(label="Tarjeta", max_length=20)
