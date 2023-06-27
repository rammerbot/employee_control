from datetime import datetime

from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from .forms import CheckForm
from django.urls import reverse_lazy
from django.contrib import messages

from .models import *
from .functions import *
from applications.personal.models import Personal

# Registro de jornadas y almuerzos
class CheckView(FormView):
    template_name = "checks/check.html"
    form_class = CheckForm
    success_url = reverse_lazy('employee_app:template')
    
    def form_valid(self, form):

        branch_form = form.cleaned_data['branch']
        card = form.cleaned_data['card']
        employee = Personal.objects.employee_browser(card)
        register = timetable()
        branch = Branch.objects.branch_browser(branch_form)

        if employee != "empty":

            if register == "entry":
                entry = EntryHour.objects.verify_or_create_entry(employee, branch)
                if entry == "success":
                    messages.success(self.request, "El Registro ha creado exitosamente")
                else:
                    messages.warning(self.request,"Ya ha sido registrada su entrada el dia de hoy")
            elif register == "lunch":
                lunch_start = LunchStart.objects.verify_or_create_start_lunch(employee, branch)
                if lunch_start == "success":
                    messages.success(self.request,"El Registro del almuerzo ha creado exitosamente")
                elif lunch_start == "too_soon":
                    messages.warning(self.request,"El Registro en la salida de almuerzo ya ha sido creado")
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
            print(lunch_start)
        else:
            messages.warning(self.request,"El Codigo es Incorrecto")
            
        return super().form_valid(form)
# Visualizacion de horas de trabajo por fechas y trabajador
class HourList(DetailView):

    template_name = "informs/inform.html"
    model = Personal
    context_object_name = "employee"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ojo, con encontrar el empleado primero...
        employee = self.object  # Reemplaza con el nombre del empleado correcto
        # Obtencion de los querysets que contienen los datos
        date = self.request.GET.get('date')
        if date:
            entry_hours = EntryHour.objects.filter(employee=employee, created__date=date).first()
            exit_hours = ExitHour.objects.filter(employee=employee, created__date=date).last()
            lunch_start = LunchStart.objects.filter(employee=employee, created__date=date).first()
            lunch_end = LunchEnd.objects.filter(employee=employee, created__date=date).first()
            if entry_hours:
                branch = entry_hours.branch
            elif exit_hours:
                branch = exit_hours.branch
            else:
                branch = "No Existe Registro"
                
            # Date Validation, valida que se seleccione una fecha antes de mostrar la informacion
        
            # Calculo de los tiempos
            if entry_hours and exit_hours:
                time_diference = entry_hours.created - exit_hours.created
                entry_hours_calc = time_diference.seconds // 3600
                entry_minuts_calc = (time_diference.seconds // 60) % 60
                context['entry_day'] = entry_hours.created.strftime('%H:%M:%S')
                context['exit_day'] = exit_hours.created.strftime('%H:%M:%S')
                context['day_hours'] = entry_hours_calc
                context['day_minuts'] = entry_minuts_calc
                context['branch'] = branch
            elif entry_hours and not exit_hours:
                context['entry_day'] = entry_hours.created.strftime('%H:%M:%S')
                context['exit_day'] = "Salida Sin Registro"
                context['day_hours'] = "Imposible Calcular Registro"
                context['day_minuts'] = "Imposible Calcular Registro"
                context['branch'] = branch
            elif not entry_hours and exit_hours:
                context['entry_day'] = "Entrada Sin Registro"
                context['exit_day'] = exit_hours.created.strftime('%H:%M:%S')
                context['day_hours'] = "Imposible Calcular Registro"
                context['day_minuts'] = "Imposible Calcular Registro"
                context['branch'] = branch
            else: 
                context['entry_day'] = 'No Existe Registro'
                context['exit_day'] = 'No Existe Registro'
                context['day_hours'] = "00"
                context['day_minuts'] = "00"
                context['branch'] = branch
            # Lunch
            if lunch_start and lunch_end:
                time_diference_lunch = lunch_end.created - lunch_start.created
                lunch_hours_calc = time_diference_lunch.seconds // 3600
                lunch_minuts_calc = (time_diference_lunch.seconds // 60) % 60 
                context['start_lunch'] = lunch_start.created.strftime('%H:%M:%S')
                context['end_lunch'] =lunch_end.created.strftime('%H:%M:%S')
                context['lunch_hours'] = lunch_hours_calc
                context['lunch_minuts'] = lunch_minuts_calc
                context['branch'] = branch
            elif lunch_start and not lunch_end:
                context['start_lunch'] = lunch_start.created.strftime('%H:%M:%S')
                context['end_luch'] = "Sin Registro de Regreso de Almuerzo"
                context['lunch_hours'] = '00'
                context['lunch_minuts'] = '00'
                context['branch'] = branch
            else:
                context['start_lunch'] = 'No Existe Registro'
                context['end_lunch'] = 'No Existe Registro'
                context['lunch_hours'] = "00"
                context['lunch_minuts'] = "00"
                context['branch'] = branch
        else:
            context['entry_day'] = 'No Existe Registro'
            context['exit_day'] = 'No Existe Registro'
            context['day_hours'] = "00"
            context['day_minuts'] = "00"
            context['start_lunch'] = 'No Existe Registro'
            context['end_lunch'] = 'No Existe Registro'
            context['lunch_hours'] = "00"
            context['lunch_minuts'] = "00"
            context['branch'] = "Realizar Busqueda por Fecha"

        return context
