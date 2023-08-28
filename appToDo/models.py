from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    apellido = models.CharField(max_length=200)

class Tarea(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=200, verbose_name= 'Título')
    descripcion = models.TextField(verbose_name= 'Descripción')
    fechaTermino = models.DateField(verbose_name= 'Fecha de Termino')
    estado = models.CharField(max_length=150, default = 'Pendiente',verbose_name= 'Estado')
    categoria = models.CharField(max_length=150, verbose_name= 'Categoría')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.id