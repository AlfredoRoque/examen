from django.urls import path,include
from apps.administrador.views import AdministradorCrear,AdministradorList,AdministradorEditar,AdministradorEliminar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r'registrar', AdministradorCrear.as_view(),name='registrar'),
    path(r'admins', login_required(AdministradorList.as_view()),name='lista_administrador'),
    path(r'editar/<pk>', login_required(AdministradorEditar.as_view()),name='modifica_administrador'),
    path(r'eliminar/<pk>', login_required(AdministradorEliminar.as_view()),name='elimina_administrador'),
    
]