from django.urls import path
from inicio.views import inicio, cargar_alumno, listado_de_alumnos, alumno_detalle, AlumnoBorrar, AlumnoActualizar

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
    path('alumnos/cargar/', cargar_alumno, name='cargar_alumno'),
    path('alumnos/<int:id_alumno>/', alumno_detalle, name='alumno_detalle'),
    path('alumnos/<int:pk>/borrar/', AlumnoBorrar.as_view(), name='alumno_borrar'),
    path('alumnos/<int:pk>/actualizar/', AlumnoActualizar.as_view(), name='alumno_actualizar')
]