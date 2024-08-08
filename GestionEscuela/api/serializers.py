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
        fields = "__all__"

class ProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = "__all__"

class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = "__all__"


class MateriasAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias_Alumno
        fields = "__all__"


class MateriasProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias_Profesor
        fields = "__all__"

