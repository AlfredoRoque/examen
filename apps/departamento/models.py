from django.db import models

from apps.empresa.models import Empresa
# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    cod = models.CharField(max_length=10,primary_key=True)
    codigo = models.ForeignKey(Empresa, null=True,blank=True, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre