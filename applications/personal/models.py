from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidades = models.CharField('Habilidades', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    def __str__(self):
        return self.habilidades


class Cargo(models.Model):
    cargo = models.CharField('Cargo', max_length=50)
    descripcion = RichTextField('Descripcion del Cargo')
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    def __str__(self):
        return self.cargo


class Personal(models.Model):
    DOCUMENT_CHOISES = [
        ('DNI', 'DNI',),
        ('CI', 'CI',),
        ('PASAPORTE', 'PASAPORTE',),
        ('CARNET DE EXTRANGERIA', 'CARNET DE EXTRANJERIA',),
    ]
   
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=50)
    fecha_nacimiento = models.DateField("Fecha de nacimiento")
    t_documento = models.CharField('Tipo de Documento',max_length=30, choices=DOCUMENT_CHOISES, default='DNI')
    n_documento = models.IntegerField('Numero de documento')
    foto = models.ImageField('Foto', upload_to='foto/')
    n_telefonico = models.IntegerField('Numero de telefono')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField('Fecha de ingreso')
    habilidades = models.ManyToManyField(Habilidades)
    aportes =  RichTextField('Aportes', blank=True)
    deficiencias = RichTextField('Deficiencias',blank=True)
    recomendaciones = RichTextField('Recomendaciones', blank=True)
    n_faltas = models.IntegerField('Numero de Faltas',blank=True, default=0)
    falta_des = RichTextField('Descripcion de faltas', blank=True)
    activo = models.BooleanField("Activo", default=True)
    curriculum = models.FileField('Curriculum', upload_to='curriculums/')
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self. first_name + ' - ' + self.last_name