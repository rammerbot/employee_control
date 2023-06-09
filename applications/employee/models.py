from django.db import models
from model_utils.models import TimeStampedModel
from .managers import *

from applications.personal.models import Personal
# Create your models here.

# Modelo de sucursales
class Branch(TimeStampedModel):
    branch = models.CharField("Sucursal", max_length=20)
    objects = BranchManager()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.branch
    
# Modelo de marcado de entradas
class EntryHour(TimeStampedModel):
    employee = models.ForeignKey(Personal, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    objects = EntryHoursManager()
    
    class Meta:
        verbose_name = "Hora de Entrada"
        verbose_name_plural = "Horas de Entrada"

    def __str__(self) -> str:
        return f"{self.employee.first_name} hora:{self.created}"
    
# Modelo de Inicio de almuerzos    
class LunchStart(TimeStampedModel):
    employee = models.ForeignKey(Personal, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    objects = LunchEstartManager()

    class Meta:
        verbose_name = "Inicio de almuerzo"
        verbose_name_plural = "Inicios de Almuerzo"
    
    def __str__(self) -> str:
        return f"{self.employee.first_name} hora:{self.created}"
    
# Modelo de final de almuerzo
class LunchEnd(TimeStampedModel):
    employee = models.ForeignKey(Personal, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    objects = LunchEndManager()
    class Meta:
        verbose_name = "Fin de Almuerzo"
        verbose_name_plural = "Fin de Almuerzo"

    def __str__(self) -> str:
        return f"{self.employee.first_name} hora:{self.created}"
    
# Modelo de marcado de salida    
class ExitHour(TimeStampedModel):
    employee = models.ForeignKey(Personal, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    objects = ExitHoursManager()

    class Meta:
        verbose_name = "Hora de Salida"
        verbose_name_plural = "Horas de Salida"

    def __str__(self) -> str:
        return f"{self.employee.first_name} hora:{self.created}"
    