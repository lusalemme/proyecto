from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Alumno
from inicio.forms import FormularioCargarAlumno, FormularioBuscarAlumno
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def cargar_alumno(request):
    print(request.POST)

    if request.method == 'POST':
        formulario = FormularioCargarAlumno(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            alumno = Alumno(nombre=info.get('nombre'), materia=info.get('materia'), nota=info.get('nota'), imagen=info.get('imagen'))
            alumno.save()

            return redirect('listado_de_alumnos')
        
    else:
        formulario = FormularioCargarAlumno()
    
    return render(request, 'cargar_alumno.html', {'formulario': formulario})

def listado_de_alumnos(request):
    formulario = FormularioBuscarAlumno(request.GET)
    alumnos_buscados = Alumno.objects.all()
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        materia_a_buscar = formulario.cleaned_data['materia']
        #nota_a_buscar = formulario.cleaned_data['nota']
        #alumnos_buscados = Alumno.objects.filter(nombre__icontains=nombre_a_buscar)
        #alumnos_buscados = Alumno.objects.filter(nombre__icontains=nombre_a_buscar, nota=nota_a_buscar)
        alumnos_buscados = Alumno.objects.filter(nombre__icontains=nombre_a_buscar, materia__icontains=materia_a_buscar)


    return render(request, 'listado_de_alumnos.html', {'alumnos_buscados': alumnos_buscados, 'formulario': formulario})

def alumno_detalle(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    return render(request, 'alumno_detalle.html', {'alumno': alumno})

def about(request):
    return render(request, 'about.html', {})

class AlumnoBorrar(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = "alumno_borrar.html"
    success_url = reverse_lazy('listado_de_alumnos')

class AlumnoActualizar(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = "alumno_actualizar.html"
    success_url = reverse_lazy('listado_de_alumnos')
    fields = '__all__'