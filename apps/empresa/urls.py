from django.urls import path,include
from apps.empresa.views import index,EmpresaCrear,EmpresaList,EmpresaEditar,EmpresaEliminar
urlpatterns = [
     path(r'', index,name='index'),
    path(r'nuevo', EmpresaCrear.as_view(),name='crear_empresa'),
    path(r'lista', EmpresaList.as_view(),name='lista_empresa'),
    path(r'editar/<pk>/', EmpresaEditar.as_view(),name='modifica_empresa'),
    path(r'eliminar/<pk>/', EmpresaEliminar.as_view(),name='elimina_empresa'),
]