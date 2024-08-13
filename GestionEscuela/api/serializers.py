from rest_framework import serializers
from GestionEscuela.models import (
    Alumnos,
    Profesores,
    Materias,
    Materias_Alumno,
    Materias_Profesor
)

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ["id", "nombre"]

class ProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = [ "id", "nombre", "materias_impartidas" ]

class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = [ "id", "nombreMateria" ]


class MateriasAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias_Alumno
        fields = [ "alumno", "nombreMateria" ]


class MateriasProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias_Profesor
        fields = [ "profesor", "nombreMateria" ]

