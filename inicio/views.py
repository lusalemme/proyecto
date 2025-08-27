from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Alumno
from inicio.forms import FormularioCargarAlumno, FormularioBuscarAlumno

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
    formulario = FormularioBuscarAlumno(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        #nota_a_buscar = formulario.cleaned_data['nota']
        alumnos_buscados = Alumno.objects.filter(nombre__icontains=nombre_a_buscar)
        #alumnos_buscados = Alumno.objects.filter(nombre__icontains=nombre_a_buscar, nota=nota_a_buscar)


    return render(request, 'listado_de_alumnos.html', {'alumnos_buscados': alumnos_buscados, 'formulario': formulario})