from django.contrib import admin
from GestionEscuela.models import(
    Alumnos,
    Profesores,
    Materias,
    Materias_Alumno,
    Materias_Profesor,
)

@admin.register(
    Alumnos,
    Profesores,
    Materias,
    Materias_Alumno,
    Materias_Profesor
)
class GestionAdmin(admin.ModelAdmin):
    pass
