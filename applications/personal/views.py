from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView
)
from django.contrib import messages
from .forms import *
from .models import Personal, Cargo, Habilidades
from django.urls import reverse_lazy

# Create your views here.

class Index_view(TemplateView):
    """vista de ventana de inicio"""

    template_name = 'home/index.html'

class List_employed(ListView):
    template_name = 'personal/list_employed.html'
    context_object_name ='personal'
    paginate_by = 5

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajador',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo,
        activo = True
        )
    
        return lista

class List_employed_off(ListView):
    template_name = 'personal/list_employed_off.html'
    context_object_name ='personas'
    paginate_by = 5

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajador',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo,
        activo = False
        )
    
        return lista

class detalle_personal(DetailView):
    template_name = "personal/detalles.html"
    context_object_name = "empleado"
    model = Personal

class Personal_departamento(ListView):
    template_name = "personal/personal_departamento.html"
    context_object_name = "personal"
    
    def get_queryset(self):
        trabajador = self.request.GET.get('trabajador',"")
        departamento = self.kwargs['departamento']
        lista = Personal.objects.filter(
            departamento_id = departamento,
            first_name__contains = trabajador
        )

        return lista

class Administrar(TemplateView):
    template_name = "personal/administrar.html"


class Administrar_empleados(ListView):
    template_name = 'personal/administrar_empleados.html'
    context_object_name ='personas'
    paginate_by = 7

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajo',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo
        )
    
        return lista

class Guardado_Exitoso(TemplateView):
    template_name = 'personal/proceso_exitoso.html'


class Crear_empleado(CreateView):
    template_name = 'personal/crear_empleado.html'
    model = Personal
    form_class = Empleado_form
    success_url =reverse_lazy('app_personal:add_empleado')
    def form_valid(self, form):
        messages.success(self.request, "Registro de empleado exitoso")
        return super().form_valid(form)


class Actualizar(UpdateView):
    template_name = 'personal/update.html'
    model = Personal
    form_class = Empleado_form
    success_url =reverse_lazy('app_personal:lista_empleados')
    def form_valid(self, form):
        messages.success(self.request, "Actualizacion exitosa Exitoso")
        return super().form_valid(form)

class Eliminar_personal(DeleteView):
    model = Personal
    template_name = "personal/eliminar_personal.html"
    success_url =reverse_lazy('app_personal:lista_empleados')
    

class Add_Cargo(CreateView):
    model = Cargo
    template_name = "personal/add_cargo.html"
    form_class = CargoForm
    success_url =reverse_lazy('app_personal:cargo')
    
    def form_valid(self, form):
        messages.success(self.request, "Registro Exitoso")
        return super().form_valid(form)


class Add_Habilidad(CreateView):
    model = Habilidades
    template_name = "personal/add_habilidad.html"
    form_class = HabilidadesForm
    success_url =reverse_lazy('app_personal:habilidad')

    def form_valid(self, form):
        messages.success(self.request, "Registro Exitoso")
        return super().form_valid(form)
