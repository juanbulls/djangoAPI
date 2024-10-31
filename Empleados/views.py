from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Empleados.models import Departamentos,Empleados
from Empleados.serializers import SerializadorDepartamentos,SerializadorEmpleado

# Create your views here.
@csrf_exempt
def departamentosApi(request, id=0):
    if request.method == 'GET':
        departamentos = Departamentos.objects.all()
        departamentos_serializador = departamentos_serializador(departamentos, many=True)
        return JsonResponse(departamentos_serializador.data, safe=False)
    elif request.method == 'POST':
        data_departamento = JSONParser().parse(request)
        departamentos_serializador = departamentos_serializador(data=data_departamento)
        if departamentos_serializador.is_valid():
            departamentos_serializador.save()
            return JsonResponse("Exitosamente added", safe=False)
        return JsonResponse('Error adding', safe=False)
    elif request == 'PUT':
        data_departamento = JSONParser().parse(request)
        departamento = Departamentos.objects.get(IdDepartamento=data_departamento['IdDepartamento'])
        departamentos_serializador = departamentos_serializador(departamento, data=data_departamento)
        if departamentos_serializador.is_valid():
            departamentos_serializador.save()
            return JsonResponse("Actualizado con exito", safe=False)
        return JsonResponse("Error actualizando", safe=False)
    elif request.method == 'DELETE':
        departamento=Departamentos.objects.get(IdDepartamento=id)
        departamento.delete()
        return JsonResponse("borrado exitosamente", safe=False)
    