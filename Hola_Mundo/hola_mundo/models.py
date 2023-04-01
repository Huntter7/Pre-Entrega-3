from django.db import models

class Tareas(models.Model):
    nombre=models.CharField(max_length=100)
    estado=models.TextField(max_length=100, default='por_hacer')
    creado_el=models.DateField(auto_now_add=True)
    modificado_el=models.DateField(auto_now=True)

    def terminar(self):
        self.estado='Terminado'

    def __str__(self):
        return f'{self.id}-{self.nombre}-{self.creado_el}'


class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_nacimieto=models.DateField()

    def __str__(self):
        return f'{self.id}-{self.nombre}-{self.apellido}'
    
class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}-{self.nombre}-{self.raza}'

