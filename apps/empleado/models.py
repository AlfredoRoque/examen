from django.db import models
from apps.empresa.models import Empresa
from apps.departamento.models import Departamento
# Create your models here.
class Sexo(models.Model):
    sexo = models.CharField(max_length=50)

    def __str__(self):
        return self.sexo

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField()
    empresa = models.ForeignKey(Empresa, null=True,blank=True, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, null=True,blank=True, on_delete=models.CASCADE)
    correo = models.CharField(max_length=50)
    sexo = models.ForeignKey(Sexo,blank=True, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    fechaIngreso = models.DateField(auto_now=True)
    curp = models.CharField(max_length=50,primary_key=True)


