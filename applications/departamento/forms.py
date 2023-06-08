from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    
    class Meta:
        model = Departamento
        fields = ('__all__')
       
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nuevo departamento...'
                }
            ),
            'short_name' : forms.TextInput(
                attrs={
                    'placeholder':'Nombre referencial...'
                }
            )
            }


