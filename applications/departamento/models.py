from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Departamento', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.short_name