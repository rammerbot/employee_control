from django.forms.models import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView
from .forms import *
from applications.personal.models import Personal
from .models import Departamento
from django.urls import reverse_lazy


# Create your views here.

class Add_departamento(LoginRequiredMixin, CreateView):
    model = Departamento
    template_name = "departamento/add_departamento.html"
    form_class = DepartamentoForm
    success_url =reverse_lazy('app_departamento:add_departamento')
    login_url = reverse_lazy('app_personal:home')

    def form_valid(self, form: BaseModelForm):
        messages.success(self.request, "Registro Exitoso")
        return super().form_valid(form)

   

class Lista_departamentos(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = "departamento/lista_departamentos.html"
    context_object_name = "departamentos"
    login_url = reverse_lazy('app_personal:home')
