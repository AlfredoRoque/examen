from django.db import models

# Create your models here.
class Administrador(models.Model):
    nombre = models.CharField(max_length=50)
    curp = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)