from django.db.models.expressions import OrderBy
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.db.models import Q
from apps.empleado.forms import EmpleadoForm
from apps.empleado.models import Empleado
from apps.departamento.models import Departamento
from apps.empresa.models import Empresa
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'empleados/index.html')
'''
def empleado_view(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/formulario_empleado.html', {'form':form})

def lista_empleado_view(request):
    empleado = Empleado.objects.all().order_by('nombre')
    contexto = {'empleados':empleado}
    return render(request,'empleados/lista_empleados.html',contexto)

def modifica_empleados(request, id_empleado):
    empleado = Empleado.objects.get(curp=id_empleado)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return redirect(lista_empleado_view)
    return render(request, 'empleados/formulario_empleado.html', {'form':form})

def elimina_empleados(request, id_empleado):
    empleado = Empleado.objects.get(curp=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect(lista_empleado_view)
    return render(request, 'empleados/empleado_eliminar.html', {'empleado':empleado})
'''

def lista_empleado_view(request):
    empleado = Empleado.objects.all().order_by('nombre')
    empresas = Empresa.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    nombre = request.GET.get('buscar')
    emp = request.GET.get('empresa')
    dep = request.GET.get('departamento')
    if emp == 'Seleccionar':
        emp = ''
    if dep == 'Seleccionar':
        dep = ''
    if nombre == '' or nombre:
        empleado = Empleado.objects.filter(
            Q(nombre__icontains = nombre)&
            Q(empresa__nombre__icontains = emp)&
            Q(departamento__nombre__icontains = dep)
        ).distinct()
        print("Hola")
        print(nombre+"--"+emp+"--"+dep)
        contexto = {'empleados':empleado,'empresas':empresas,'departamentos':departamentos}
    else:
        print("Hola22")
        contexto = {'empleados':empleado,'empresas':empresas,'departamentos':departamentos}
    return render(request,'empleados/lista_empleados.html',contexto)


class EmpleadosList(ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'

class EmpleadoCrear(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/formulario_empleado.html'
    success_url =reverse_lazy('lista_empleado')

class EmpleadoEditar(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/formulario_empleado.html'
    success_url =reverse_lazy('lista_empleado')

class EmpleadoEliminar(DeleteView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_eliminar.html'
    success_url =reverse_lazy('lista_empleado')