from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
    FormView
)
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import *
from .models import Personal, Cargo, Habilidades
from django.urls import reverse_lazy

# Inicio de sesion
class IndexView(FormView):
    template_name = 'home/index.html'
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
            return self.form_invalid(form)
        
# cerrar sesion
class Logout(LogoutView):
    next_page = reverse_lazy("app_personal:home")
        
# Lista de Empleados
class List_employed(LoginRequiredMixin, ListView):
    template_name = 'personal/list_employed.html'
    context_object_name ='personal'
    paginate_by = 5
    login_url = reverse_lazy('app_personal:home')

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajador',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo,
        activo = True
        )
    
        return lista

# Lista de Empleados Deshabilitados
class List_employed_off(LoginRequiredMixin,ListView):
    template_name = 'personal/list_employed_off.html'
    context_object_name ='personas'
    paginate_by = 5
    login_url = reverse_lazy('app_personal:home')

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajador',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo,
        activo = False
        )
    
        return lista

# Detalles de empleados
class detalle_personal(LoginRequiredMixin, DetailView):
    template_name = "personal/detalles.html"
    context_object_name = "empleado"
    model = Personal
    login_url = reverse_lazy('app_personal:home')

# Personal por departamentos
class Personal_departamento(LoginRequiredMixin, ListView):
    template_name = "personal/personal_departamento.html"
    context_object_name = "personal"
    login_url = reverse_lazy('app_personal:home')
    
    def get_queryset(self):
        trabajador = self.request.GET.get('trabajador',"")
        departamento = self.kwargs['departamento']
        lista = Personal.objects.filter(
            departamento_id = departamento,
            first_name__contains = trabajador
        )

        return lista

# vista de administracion de departamentos, cargos y habilidades
class Administrar(LoginRequiredMixin,TemplateView):
    template_name = "personal/administrar.html"
    login_url = reverse_lazy('app_personal:home')

# vista previa para editar o inhabilitar empleados
class Administrar_empleados(LoginRequiredMixin, ListView):
    template_name = 'personal/administrar_empleados.html'
    context_object_name ='personas'
    paginate_by = 7
    login_url = reverse_lazy('app_personal:home')

    def get_queryset(self):
        trabajo = self.request.GET.get('trabajo',"")
        lista = Personal.objects.filter(
        first_name__contains = trabajo
        )
    
        return lista

# Cargar empleados nuevos al sistema
class Crear_empleado(LoginRequiredMixin,CreateView):
    template_name = 'personal/crear_empleado.html'
    model = Personal
    form_class = Empleado_form
    success_url =reverse_lazy('app_personal:add_empleado')
    login_url = reverse_lazy('app_personal:home')
    def form_valid(self, form):
        messages.success(self.request, "Registro de empleado exitoso")
        return super().form_valid(form)

# Actualizar empleados
class Actualizar(LoginRequiredMixin, UpdateView):
    template_name = 'personal/update.html'
    model = Personal
    form_class = Empleado_form
    login_url = reverse_lazy('app_personal:home')
    success_url =reverse_lazy('app_personal:lista_empleados')
    def form_valid(self, form):
        messages.success(self.request, "Actualizacion exitosa Exitoso")
        return super().form_valid(form)

# Eliminar empleados
class Eliminar_personal(LoginRequiredMixin, DeleteView):
    model = Personal
    template_name = "personal/eliminar_personal.html"
    success_url =reverse_lazy('app_personal:lista_empleados')
    login_url = reverse_lazy('app_personal:home')
    
# Agregar cargos
class Add_Cargo(LoginRequiredMixin, CreateView):
    model = Cargo
    template_name = "personal/add_cargo.html"
    form_class = CargoForm
    success_url =reverse_lazy('app_personal:cargo')
    login_url = reverse_lazy('app_personal:home')
    
    def form_valid(self, form):
        messages.success(self.request, "Registro Exitoso")
        return super().form_valid(form)

# Agregar habilidades
class Add_Habilidad(LoginRequiredMixin, CreateView):
    model = Habilidades
    template_name = "personal/add_habilidad.html"
    form_class = HabilidadesForm
    success_url =reverse_lazy('app_personal:habilidad')
    login_url = reverse_lazy('app_personal:home')

    def form_valid(self, form):
        messages.success(self.request, "Registro Exitoso")
        return super().form_valid(form)
