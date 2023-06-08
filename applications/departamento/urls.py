from django.urls import path
from . import views

app_name = 'app_departamento'

urlpatterns = [
    path('add_departamento/', views.Add_departamento.as_view(), name='add_departamento'),
    path('departamentos/', views.Lista_departamentos.as_view(), name="departamentos")

]
