from django.core.management.base import BaseCommand
from faker import Faker
import random
from apps.alumno.models import Alumno
from apps.profesor.models import Profesor
from apps.materia.models import Materia
from apps.cicloLectivo.models import CicloLectivo
from apps.asignacion.models import Asignacion
from apps.cursada.models import Cursada
from apps.evento.models import Evento, Tipo, Estado

class Command(BaseCommand):
    help = 'Genera datos ficticios para la base de datos'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear Tipos y Estados de Evento para referencias
        tipos = ["Examen", "Trabajo Práctico", "Aviso General", "Calificación"]
        estados = ["Activo", "Archivado", "Eliminado"]

        tipo_objs = [Tipo.objects.get_or_create(nombre=nombre)[0] for nombre in tipos]
        estado_objs = [Estado.objects.get_or_create(nombre=nombre)[0] for nombre in estados]

        # Crear Profesores
        for _ in range(5):
            Profesor.objects.create(
                legajo=fake.unique.random_int(min=1000, max=9999),
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                email=fake.unique.email(),
                telefono=fake.phone_number()
            )

        # Crear Alumnos
        for _ in range(20):
            Alumno.objects.create(
                numeroLegajo=fake.unique.random_int(min=1000, max=9999),
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                email=fake.unique.email(),
                telefono=fake.phone_number(),
                estado=random.choice([True, False])
            )

        # Crear Materias
        for _ in range(10):
            Materia.objects.create(
                codigo=fake.unique.bothify(text='MAT-###'),
                nombre=fake.word().capitalize(),
                descripcion=fake.sentence(nb_words=10)
            )

        # Crear Ciclos Lectivos
        for _ in range(2):
            CicloLectivo.objects.create(
                anio=fake.year(),
                periodo=random.choice(["Anual", "Primer Cuatrimestre", "Segundo Cuatrimestre"]),
                fechaInicio=fake.date_between(start_date='-2y', end_date='today'),
                fechaFin=fake.date_between(start_date='today', end_date='+2y'),
                estado=random.choice([True, False])
            )

        # Crear Asignaciones
        profesores = Profesor.objects.all()
        materias = Materia.objects.all()
        ciclos = CicloLectivo.objects.all()

        for _ in range(15):
            Asignacion.objects.create(
                profesor=random.choice(profesores),
                materia=random.choice(materias),
                cicloLectivo=random.choice(ciclos)
            )

        # Crear Cursadas
        alumnos = Alumno.objects.all()
        for _ in range(20):
            Cursada.objects.create(
                alumno=random.choice(alumnos),
                ciclolectivo=random.choice(ciclos),
                materia=random.choice(materias),
                estado=random.choice([True, False]),
                fecha_inscripcion=fake.date_between(start_date='-1y', end_date='today')
            )

        # Crear Eventos
        for _ in range(10):
            Evento.objects.create(
                profesor=random.choice(profesores),
                materia=random.choice(materias),
                tipo=random.choice(tipo_objs),
                estado=random.choice(estado_objs),
                titulo=fake.sentence(nb_words=5),
                descripcion=fake.text(max_nb_chars=200),
                fecha_creacion=fake.date_this_year(),
                fecha_vencimiento=fake.date_between(start_date='today', end_date='+30d')
            )

        self.stdout.write(self.style.SUCCESS('Datos ficticios generados exitosamente.'))
