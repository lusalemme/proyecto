from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    nota = models.IntegerField()
    imagen = models.ImageField(upload_to="imagenes_examenes", null=True)

    def __str__(self):
        return f'nombre: {self.nombre} // materia: {self.materia}'