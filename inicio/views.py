from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Alumno
from inicio.forms import FormularioCargarAlumno

def inicio(request):
    return render(request, 'inicio.html')

def cargar_alumno(request):
    print(request.POST)

    if request.method == 'POST':
        formulario = FormularioCargarAlumno(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            alumno = Alumno(nombre=info.get('nombre'), nota=info.get('nota'))
            alumno.save()

            return redirect('listado_de_alumnos')
        
    else:
        formulario = FormularioCargarAlumno()
    
    return render(request, 'cargar_alumno.html', {'formulario': formulario})

def listado_de_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listado_de_alumnos.html', {'alumnos': alumnos})