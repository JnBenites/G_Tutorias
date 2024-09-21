from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class docente(models.Model):
    id_docentes = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id_docentes} - {self.id_user.first_name} {self.id_user.last_name}'

# Create your models here.
class estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id_estudiante} - {self.id_user.first_name} {self.id_user.last_name}'