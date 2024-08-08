from rest_framework.routers import DefaultRouter
from GestionEscuela.api.views import (
    AlumnosApiViewSet,
    ProfesoresApiViewSet,
    MateriasApiViewSet,
    MateriasAlumnoApiViewSet,
    MateriasProfesorApiViewSet
)


router_alumnos = DefaultRouter()
router_alumnos.register(
    prefix="alumnos", basename="alumnos", viewset=AlumnosApiViewSet
)

router_profesores = DefaultRouter()
router_profesores.register(
    prefix="profesores", basename="profesores", viewset=ProfesoresApiViewSet
)

router_materias = DefaultRouter()
router_materias.register(
    prefix="materias", basename="materias", viewset=MateriasApiViewSet
)

router_materiasAlumno = DefaultRouter()
router_materiasAlumno.register(
    prefix="materiasAlumno", basename="materiasAlumno", viewset=MateriasAlumnoApiViewSet
)


router_materiasProfesor = DefaultRouter()
router_materiasProfesor .register(
    prefix="materiasProfesor ", basename="materiasProfesor ", viewset=MateriasProfesorApiViewSet
)
