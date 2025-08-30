from django import forms

class FormularioCargarAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    materia = forms.CharField(max_length=20)
    nota = forms.IntegerField()
    imagen = forms.ImageField(required=False)

class FormularioBuscarAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    materia = forms.CharField(max_length=20, required=False)
    #nota = forms.IntegerField(required=False)