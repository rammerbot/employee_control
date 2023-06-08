from .models import Departamento

def get_departamento(request):
    departamentos = Departamento.objects.all()

    return {
        'get_departamento': departamentos
    }