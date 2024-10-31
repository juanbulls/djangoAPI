from django.db import models

# Create your models here.

class Departamentos(models.Model):
    IdDepartamento = models.AutoField(primary_key=True)
    NombreDepartamento = models.CharField(max_length=500)

class Empleados(models.Model):
    IdEmpleado = models.AutoField(primary_key=True)
    NombreEmpleado = models.CharField(max_length=500)
    Departamento = models.CharField(max_length=500)
    FechaDeIngreso = models.DateField() 
    NombreArchivoFoto = models.CharField(max_length=500)