from django import forms

class FormularioCargarAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    nota = forms.IntegerField()