from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioWeb(AbstractUser):

    fecha_nacimiento    = models.DateField(verbose_name='fecha de nacimiento', null=True) 

    class Meta:
        managed = True
        db_table = 'usuarioweb'
