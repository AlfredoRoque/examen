from django.urls import path,include
from apps.empresa.views import index,EmpresaCrear,EmpresaList,EmpresaEditar,EmpresaEliminar
from django.contrib.auth.decorators import login_required
urlpatterns = [
     path(r'', login_required(index),name='index'),
    path(r'nuevo', login_required(EmpresaCrear.as_view()),name='crear_empresa'),
    path(r'lista', login_required(EmpresaList.as_view()),name='lista_empresa'),
    path(r'editar/<pk>/', login_required(EmpresaEditar.as_view()),name='modifica_empresa'),
    path(r'eliminar/<pk>/', login_required(EmpresaEliminar.as_view()),name='elimina_empresa'),
]