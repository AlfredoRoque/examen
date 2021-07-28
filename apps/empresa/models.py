from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,primary_key=True)
    descripcion = models.CharField(max_length=100)
    

    def ___str___(self):
        return '{}'.format(self.nombre)