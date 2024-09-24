from django.db import models

# Create your models here.
class carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.id_carrera} - {self.nombre_carrera}'

class ciclo(models.Model):
    id_ciclo =  models.AutoField(primary_key=True)
    nombre_ciclo = models.CharField(max_length=50)
    def __str__(self): 
        return f'{self.id_ciclo} - {self.nombre_ciclo}'