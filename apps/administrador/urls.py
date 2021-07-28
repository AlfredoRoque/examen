from django.urls import path,include
from apps.administrador.views import AdministradorCrear,AdministradorList,AdministradorEditar,AdministradorEliminar

urlpatterns = [
    path(r'registrar', AdministradorCrear.as_view(),name='registrar'),
    path(r'admins', AdministradorList.as_view(),name='lista_administrador'),
    path(r'editar/<pk>', AdministradorEditar.as_view(),name='modifica_administrador'),
    path(r'eliminar/<pk>', AdministradorEliminar.as_view(),name='elimina_administrador'),
    
]