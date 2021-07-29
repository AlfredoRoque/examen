from django.db.models.expressions import OrderBy
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.db.models import Q
from apps.empresa.forms import EmpresaForm
from apps.empresa.models import Empresa
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'empresa/lista_empresa.html')
class EmpresaList(ListView):
    model = Empresa
    template_name = 'empresa/lista_empresa.html'

class EmpresaCrear(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/formulario_empresa.html'
    success_url =reverse_lazy('lista_empresa')

class EmpresaEditar(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/formulario_empresa.html'
    success_url =reverse_lazy('lista_empresa')

class EmpresaEliminar(DeleteView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_eliminar.html'
    success_url =reverse_lazy('lista_empresa')