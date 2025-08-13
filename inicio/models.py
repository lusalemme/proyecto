from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    nota = models.IntegerField()

    def __str__(self):
        return f'nombre: {self.nombre}, nota: {self.nota}'