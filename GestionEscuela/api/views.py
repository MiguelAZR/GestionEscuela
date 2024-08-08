from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

from GestionEscuela.models import (
    Alumnos,
    Profesores,
    Materias,
    Materias_Alumno,
    Materias_Profesor
)
from GestionEscuela.api.serializers import (
    AlumnosSerializer,
    ProfesoresSerializer,
    MateriasSerializer,
    MateriasAlumnoSerializer,
    MateriasProfesorSerializer
)

from GestionEscuela.api.serializers import MateriasAlumnoSerializer

class AlumnosApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = AlumnosSerializer
    queryset = Alumnos.objects.all()

class ProfesoresApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = ProfesoresSerializer
    queryset = Profesores.objects.all()

class MateriasApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = MateriasSerializer
    queryset = Materias.objects.all()

class MateriasAlumnoApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = MateriasAlumnoSerializer
    queryset = Materias_Alumno.objects.all()

    @action(
        detail=False,
        methods=["get"],
        url_path=r"byIdAlumno/(?P<IdAlumno>\w+)",
    )
    def getMateriasByAlumno(self,request,IdAlumno=None):
        alumno = Materias_Alumno.objects.filter(alumno=IdAlumno)
        serializer = MateriasAlumnoSerializer(alumno, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

class MateriasProfesorApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = MateriasProfesorSerializer
    queryset = Materias_Profesor.objects.filter(profesor__disponible=True)

    @action(
        detail=False,
        methods=["get"],
        url_path=r"byIdProfesor/(?P<IdProfesor>\w+)",
    )
    def getMateriasByProfesor(self,request,IdProfesor=None):
        profesor = Materias_Profesor.objects.filter(profesor=IdProfesor)
        serializer = MateriasProfesorSerializer(profesor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
