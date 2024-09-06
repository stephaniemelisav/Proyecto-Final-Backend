from rest_framework import viewsets
from .models import Alumno
from .serializer import AlumnoSerializer
# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

#Esta vista te permite listar todos los libros existentes y crear nuevos libros a través de la API. 
# Además, el serializer se encargará de convertir el modelo a JSON.