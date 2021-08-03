from django.urls import path,include
from apps.departamento.views import index,DepartamentoList,DepartamentoCrear,DepartamentoEditar,DepartamentoEliminar
from django.contrib.auth.decorators import login_required

urlpatterns = [
     path(r'', login_required(index),name='index'),
    path(r'nuevo', login_required(DepartamentoCrear.as_view()),name='crear_departamento'),
    path(r'lista', login_required(DepartamentoList.as_view()),name='lista_departamento'),
    path(r'editar/<pk>/', login_required(DepartamentoEditar.as_view()),name='modifica_departamento'),
    path(r'eliminar/<pk>/', login_required(DepartamentoEliminar.as_view()),name='elimina_departamento'),
]