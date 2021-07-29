from django.db.models.expressions import OrderBy
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.db.models import Q
from apps.departamento.forms import DepartamentoForm
from apps.departamento.models import Departamento
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'departamento/lista_departamento.html')
class DepartamentoList(ListView):
    model = Departamento
    template_name = 'departamento/lista_departamento.html'

class DepartamentoCrear(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/formulario_departamento.html'
    success_url =reverse_lazy('lista_departamento')

class DepartamentoEditar(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/formulario_departamento.html'
    success_url =reverse_lazy('lista_departamento')

class DepartamentoEliminar(DeleteView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_eliminar.html'
    success_url =reverse_lazy('lista_departamento')