from django.urls import path
from inicio.views import inicio, cargar_alumno, listado_de_alumnos

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
    path('alumnos/cargar/', cargar_alumno, name='cargar_alumno')
]