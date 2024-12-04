from django.urls import path
from .views import ListaAlumnos, DetalleAlumno, CrearAlumno, EditarAlumno, EliminarAlumno

urlpatterns = [
    path('alumnos/', ListaAlumnos.as_view(), name='lista-alumnos'),
    path('alumno/detalle/<int:pk>/', DetalleAlumno.as_view(), name='detalle-alumno'),
    path('alumno/crear/', CrearAlumno.as_view(), name='crear-alumno'),
    path('alumno/editar/<int:pk>/', EditarAlumno.as_view(), name='editar-alumno'),
    path('alumno/eliminar/<int:pk>/', EliminarAlumno.as_view(), name='eliminar-alumno'),
]