from django.urls import path,include
from apps.empleado.views import index,lista_empleado_view,EmpleadoCrear,EmpleadoEditar,EmpleadoEliminar
urlpatterns = [
    path(r'', index,name='index'),
    path(r'nuevo', EmpleadoCrear.as_view(),name='crear_empleado'),
    path(r'lista', lista_empleado_view,name='lista_empleado'),
    path(r'editar/<pk>/', EmpleadoEditar.as_view(),name='modifica_empleado'),
    path(r'eliminar/<pk>/', EmpleadoEliminar.as_view(),name='elimina_empleado'),
]