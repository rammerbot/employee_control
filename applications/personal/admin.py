from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',

    )
    search_fields = ('first_name',)
    list_filter = ('departamento','habilidades' )
    filter_horizontal = ('habilidades',)

admin.site.register(Personal, EmpleadoAdmin)
admin.site.register(Cargo)