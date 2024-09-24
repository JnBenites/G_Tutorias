from django.db import models
from django.contrib.auth.models import User
from carrera.models import carrera, ciclo

# Create your models here.
class docente(models.Model):
    id_docentes = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id_docentes} - {self.id_user.first_name} {self.id_user.last_name}'

class estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id_estudiante} - {self.id_user.first_name} {self.id_user.last_name}'

class disponibilidad(models.Model):
    id_disponibilidad = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    rango_hora_inicio = models.TimeField()
    rango_hora_fin = models.TimeField()
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]
    dia = models.CharField(
        max_length=3,
        choices=DIAS_SEMANA,
        default='LUN'
    )
    def __str__(self):
        return f'{self.id_disponibilidad} - {self.fecha_inicio} - {self.fecha_fin} - {self.rango_hora_inicio}- {self.rango_hora_fin} - {self.dia}'


class estado_solicitud(models.Model):
    id_estado_solicitud =  models.AutoField(primary_key=True)
    estado  = models.CharField(max_length=50, null=False)
    def __str__(self):
        return f'{self.id_estado_solicitud} - {self.estado}'

class solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(estudiante, on_delete=models.PROTECT, null=False)
    id_disponibilidad = models.ForeignKey(disponibilidad, on_delete=models.PROTECT, null=False)
    id_estado = models.ForeignKey(estado_solicitud,  on_delete=models.PROTECT, null=False)
    fecha_solicitud = models.DateField(null=True, blank=True)
    fecha_contestacion  =  models.DateField(null=True, blank=True)
    def __str__(self):
        return f'{self.id_solicitud} - {self.id_estudiante} - {self.id_disponibilidad} - {self.id_estado}'

class asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=100)
    id_carrera = models.ForeignKey(carrera, on_delete=models.PROTECT, null=False)
    id_ciclo = models.ForeignKey(ciclo, on_delete=models.PROTECT,   null=False)
    id_disponibilidad = models.ForeignKey(disponibilidad, on_delete=models.SET_NULL, null=True)
    id_solicitudes = models.ForeignKey(solicitud, on_delete=models.SET_NULL, null=True)
    def __str__(self): 
        return f'{self.id_asignatura} - {self.nombre_asignatura} - {self.id_ciclo}'