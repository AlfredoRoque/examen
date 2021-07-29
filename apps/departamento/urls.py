from django.urls import path,include
from apps.departamento.views import index,DepartamentoList,DepartamentoCrear,DepartamentoEditar,DepartamentoEliminar
urlpatterns = [
     path(r'', index,name='index'),
    path(r'nuevo', DepartamentoCrear.as_view(),name='crear_departamento'),
    path(r'lista', DepartamentoList.as_view(),name='lista_departamento'),
    path(r'editar/<pk>/', DepartamentoEditar.as_view(),name='modifica_departamento'),
    path(r'eliminar/<pk>/', DepartamentoEliminar.as_view(),name='elimina_departamento'),
]