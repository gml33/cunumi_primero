from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    edad = models.IntegerField(blank=True)
    diagnostico_presuntivo = models.CharField(max_length=200, blank=True)
    motivo_consulta = models.CharField(max_length=200, blank=True)
    derivado = models.BooleanField(default=False)
    detalle_derivacion = models.CharField(max_length=200, blank=True)
    dni = models.CharField(max_length=100, blank=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

    estado = models.CharField(blank=True, null=True)
    estado_choices = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo'),
        ('alta', 'alta'),
        ('derivado', 'derivado')
    )
    estado = models.CharField(
        max_length=20, choices=estado_choices, default='activo')
    imagen = models.ImageField(upload_to='pacientes', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class historiaClinica(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='Hc', blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class evolucion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='evoluciones', blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class derivacion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    motivo = models.TextField(blank=True)
    profesional = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='derivaciones', blank=True)
