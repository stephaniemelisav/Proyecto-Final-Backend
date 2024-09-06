from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet, basename='alumno')

urlpatterns=[
    path('', include(router.urls)),
]


