from rest_framework import serializers
from Empleados.models import Departamentos,Empleados

class SerializadorDepartamentos(serializers.ModelSerializer):
    class Meta:
        model=Departamentos
        fields=('IdDepartamento', 'NombreDepartamento')

class SerializadorEmpleado(serializers.ModelSerializer):
    class Meta:
        model=Empleados
        fields=('IdEmpleado','NombreEmpleado','Departamento','FechaDeIngreso','NombreArchivoFoto')