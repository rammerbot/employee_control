from django.urls import path
from . import views

app_name = 'app_personal'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name="home"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('list_employed/', views.List_employed.as_view(), name='lista_empleados'),
    path('list_employed_off/', views.List_employed_off.as_view(), name='lista_empleados_off'),
    path('add_empleado/', views.Crear_empleado.as_view(), name='add_empleado'),
    path('detalles/<pk>/', views.detalle_personal.as_view(),name='detalle_personal'),
    path('departamento_personal/<departamento>', views.Personal_departamento.as_view(), name='departamento_personal'),
    path('administrar/', views.Administrar.as_view(), name='administrar'),
    path('administrar_empleados/', views.Administrar_empleados.as_view(), name='administrar_empleados'),
    path('actualizar/<pk>', views.Actualizar.as_view(), name='actualizar'),
    path('eliminar/<pk>', views.Eliminar_personal.as_view(),name='eliminar'),
    path('cargo/', views.Add_Cargo.as_view(),name='cargo'),
    path('add_habilidad/', views.Add_Habilidad.as_view(),name='habilidad'),
]