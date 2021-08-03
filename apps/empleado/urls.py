from django.urls import path,include
from apps.empleado.views import index,lista_empleado_view,EmpleadoCrear,EmpleadoEditar,EmpleadoEliminar
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path(r'', login_required(index),name='index'),
    path(r'nuevo', login_required(EmpleadoCrear.as_view()),name='crear_empleado'),
    path(r'lista', login_required(lista_empleado_view),name='lista_empleado'),
    path(r'editar/<pk>/', login_required(EmpleadoEditar.as_view()),name='modifica_empleado'),
    path(r'eliminar/<pk>/', login_required(EmpleadoEliminar.as_view()),name='elimina_empleado'),
]