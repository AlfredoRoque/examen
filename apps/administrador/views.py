from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from apps.administrador.form import RegistroForm

# Create your views here.
'''
def index(request):
    return render(request, 'administrador/lista_administrador.html')
'''
class AdministradorList(ListView):
    model = User
    template_name = 'administrador/lista_administrador.html'

class AdministradorCrear(CreateView):
    template_name = 'administrador/formulario_administrador.html'
    form_class = RegistroForm
    success_url =reverse_lazy('lista_administrador')

class AdministradorEditar(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'administrador/formulario_administrador.html'
    success_url =reverse_lazy('lista_administrador')

class AdministradorEliminar(DeleteView):
    model = User
    form_class = RegistroForm
    template_name = 'administrador/administrador_eliminar.html'
    success_url =reverse_lazy('lista_administrador')
