from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Alumno

class ListaAlumnos(ListView):
    model = Alumno
    template_name = 'alumnos_lista.html'
    context_object_name = 'alumnos'
    ordering = ['apellido', 'nombre']

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = 'alumno.html'
    context_object_name = 'alumno'

class CrearAlumno(CreateView):
    model = Alumno
    template_name = 'alumno_formulario.html'
    fields = ['numeroLegajo', 'nombre', 'apellido', 'email', 'telefono', 'estado']
    success_url = reverse_lazy('lista-alumnos')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno creado exitosamente.')
        return super().form_valid(form)

class EditarAlumno(UpdateView):
    model = Alumno
    template_name = 'alumno_formulario.html'
    fields = ['numeroLegajo', 'nombre', 'apellido', 'email', 'telefono', 'estado']
    success_url = reverse_lazy('lista-alumnos')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno modificado exitosamente.')
        return super().form_valid(form)

class EliminarAlumno(DeleteView):
    model = Alumno
    template_name = 'confirmar_borrar_alumno.html'
    success_url = reverse_lazy('lista-alumnos')
    context_object_name = 'alumno'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, f'El alumno {self.object.nombre} {self.object.apellido} ha sido borrado exitosamente.')
        return HttpResponseRedirect(success_url)