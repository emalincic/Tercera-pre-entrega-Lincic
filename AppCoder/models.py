from django.db import models


class Deporte(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    juego = models.CharField(max_length=50, choices=[('I', 'Individual'), ('C', 'Colectivo'), ('M', 'Mixto')])


def __str__(self):
    return f"Deporte: {self.nombre}, modo de juego: {self.juego}"


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=50)


def __str__(self):
    return f"Equipo: {self.nombre} Ciudad: {self.ciudad}"


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)


def __str__(self):
    return f"El jugador: {self.nombre} {self.apellido}, juega en {self.equipo} en la posición de {self.posicion}"
