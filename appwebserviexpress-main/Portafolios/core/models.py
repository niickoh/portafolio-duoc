# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from usuarios.models import UsuarioWeb
from django.db import models
from django.contrib.auth.models import AbstractUser


class Boleta(models.Model):
    id = models.BigAutoField(primary_key=True)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE,)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=100, blank=True, null=True)
    total = models.IntegerField()
    id_user = models.IntegerField()
    nombre_cliente = models.CharField(max_length=100)
    nombre_servicio = models.CharField(max_length=30)    
    nombre_mecanico = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta'


class Reservadehora(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_solicitud = models.DateTimeField()
    asunto = models.CharField(max_length=200)
    tiposervicio = models.ForeignKey('Tiposervicio', on_delete=models.CASCADE)
    usuarioescritorio = models.ForeignKey('Usuarioescritorio', on_delete=models.CASCADE)
    usuarioweb = models.ForeignKey(UsuarioWeb, on_delete=models.CASCADE, related_name='reserva')

    class Meta:
        managed = True
        db_table = 'reservadehora'


class Servicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=200, blank=True, null=True)
    validado = models.BooleanField()
    reservadehora = models.ForeignKey(Reservadehora, on_delete=models.CASCADE)
    

    class Meta:
        managed = False
        db_table = 'servicio'


class Tiposervicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tiposervicio'


class Tipousuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Usuarioescritorio(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipousuario = models.ForeignKey(Tipousuario, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    primer_nombre = models.CharField(max_length=150)
    segundo_nombre = models.CharField(max_length=150, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        nombre = self.primer_nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
        return nombre

    class Meta:
        managed = False
        db_table = 'usuarioescritorio'