from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class Empleado_form(forms.ModelForm):
    
    class Meta:
        model = Personal
        fields = ('__all__')
       
        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple(),
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre...'
                }
            ),
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre...'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese apellido...'
                }
            ),
            'fecha_nacimiento' : forms.TextInput(
                attrs={
                    'placeholder':'Fecha de nacimiento...'
                }
            ),
            'n_documento' : forms.TextInput(
                attrs={
                    'placeholder':'N° de documento...'
                }
            ),
            'n_telefonico' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese telefono...'
                }
            ),
            'fecha_ingreso' : forms.TextInput(
                attrs={
                    'placeholder':'Fecha de ingreso...'
                }
            ),
            'n_faltas' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese N° de faltas...'
                }
            )
            }

class HabilidadesForm(forms.ModelForm):
    
    class Meta:
        model = Habilidades
        fields = ('__all__')
       
        widgets = {
            'habilidades' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nueva habilidad...'
                }
            )
            }

class CargoForm(forms.ModelForm):
    
    class Meta:
        model = Cargo
        fields = ('__all__')
       
        widgets = {
            'cargo' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre del cargo...'
                }
            )
            }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
