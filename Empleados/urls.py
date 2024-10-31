from django.urls import path, re_path  # Update the import
from Empleados import views

urlpatterns = [
    path('departamento', views.departamentosApi),  # Using path
    re_path(r'^departamento/([0-9]+)$', views.departamentoDetailApi)  # Using re_path for regex
]
