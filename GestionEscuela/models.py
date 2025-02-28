from django.db import models


class Materias(models.Model):
    nombreMateria = models.CharField(max_length=30, blank=True, null=False)


class Alumnos(models.Model):
    nombre = models.CharField(max_length=70, blank=True, null=False)
    apellido_paterno = models.CharField(max_length=70, blank=True, null=False)
    apellido_materno = models.CharField(max_length=70, blank=True, null=False)
    

class Profesores(models.Model):
    nombre = models.CharField(max_length=70, blank=True, null=False)
    apellido_paterno = models.CharField(max_length=70, blank=True, null=False)
    apellido_materno = models.CharField(max_length=70, blank=True, null=False)
    disponible = models.BooleanField(blank=True, null=True)


class Materias_Alumno(models.Model):
    alumno = models.ForeignKey(
        Alumnos, on_delete=models.CASCADE, blank=True, null=True
    )
    materias = models.ForeignKey(
        Materias, on_delete=models.CASCADE, blank=True, null=True
    )


class Materias_Profesor(models.Model):
    profesor = models.ForeignKey(
        Profesores, on_delete=models.CASCADE, blank=True, null=True
    )
    materias = models.ForeignKey(
        Materias, on_delete=models.CASCADE, blank=True, null=True
    )


