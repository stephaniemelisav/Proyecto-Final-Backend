from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Alumno

class ListaAlumnos(ListView):
    model = Alumno
    template_name = 'alumnos/lista_alumnos.html'
    context_object_name = 'alumnos'
    ordering = ['apellido', 'nombre']

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = 'alumnos/detalle_alumno.html'
    context_object_name = 'alumno'

class CrearAlumno(CreateView):
    model = Alumno
    template_name = 'alumnos/formulario_alumno.html'
    fields = ['numeroLegajo', 'nombre', 'apellido', 'email', 'telefono', 'estado']
    success_url = reverse_lazy('lista-alumnos')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno creado exitosamente.')
        return super().form_valid(form)

class EditarAlumno(UpdateView):
    model = Alumno
    template_name = 'alumnos/formulario_alumno.html'
    fields = ['numeroLegajo', 'nombre', 'apellido', 'email', 'telefono', 'estado']
    success_url = reverse_lazy('lista-alumnos')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno actualizado exitosamente.')
        return super().form_valid(form)

class EliminarAlumno(DeleteView):
    model = Alumno
    template_name = 'alumnos/confirmar_eliminar_alumno.html'
    success_url = reverse_lazy('lista-alumnos')
    context_object_name = 'alumno'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Alumno eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)