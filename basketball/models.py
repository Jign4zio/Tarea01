from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Team(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/')
    codigo = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.nombre

class Player(models.Model):
    nombreplayer = models.CharField(max_length=50)
    apodo = models.CharField(max_length=20)
    fnacimiento = models.IntegerField()
    edad = models.IntegerField()
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    estatura = models.FloatField()
    peso = models.FloatField()
    foto = models.ImageField(upload_to='photo/%Y/%m/%d/')
    posicion = models.CharField(max_length=8)
    team = models.ManyToManyField('Team')

    def __str__(self):
        return self.nombreplayer

class Coach(models.Model):
    nombreentrenador = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.CharField(max_length=99)
    rut = models.CharField(max_length=12)
    apodo = models.CharField(max_length=15)

    def __str__(self):
        return self.nombreentrenador

class Partido (models.Model):
    nombrepartido = models.CharField(max_length=99)
