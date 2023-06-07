from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import CheckForm
from django.urls import reverse_lazy
from django.contrib import messages

from .models import *
from .functions import *

# Create your views here.


class CheckView(FormView):
    template_name = "checks/check.html"
    form_class = CheckForm
    success_url = reverse_lazy('employee_app:template')
    
    def form_valid(self, form):

        branch_form = form.cleaned_data['branch']
        card = form.cleaned_data['card']
        employee = Employee.objects.employee_browser(card)
        register = timetable()
        branch = Branch.objects.branch_browser(branch_form)

        if register == "entry":
            entry = EntryHour.objects.verify_or_create_entry(employee, branch)
            if entry == "success":
                messages.success(self.request, "El Registro ha creado exitosamente")
            else:
                messages.warning(self.request,"Ya ha sido registrada su entrada el dia de hoy")
        elif register == "lunch":
            lunch_start = LunchStart.objects.verify_or_create_start_lunch(employee, branch)
            if lunch_start == "success":
                messages.warning(self.request,"El Registro del almuerzo ha creado exitosamente")
            elif lunch_start == "created":
                luch_end = LunchEnd.objects.verify_or_create_end_lunch(employee, branch)
                if luch_end == "success":
                    messages.success(self.request,"Se registro correctamente el regreso del Almuerzo")
                elif luch_end == "created":
                    messages.warning(self.request,"El registro de regreso de almuerzo ya ha sido creado anteriormente")
        elif register == "exit":
            exit_register =  ExitHour.objects.verify_or_create_exit(employee, branch)
            if exit_register == "success":
                messages.success(self.request,"El Registro ha creado exitosamente")
            elif exit_register == "created":
                messages.warning(self.request,"Ya ha sido registrada su salida el dia de hoy")
            
        return super().form_valid(form)


