from django.db import models
import datetime

class Usuario(models.Model): # Heredamos lo que tiene Model.
    nombre = models.CharField('Nombre de la persona',max_length=20) # Se crea el campo con el nombre, tipo y su longitud.
    apellido = models.CharField('Apellido de la persona',max_length=10)
    product = models.ManyToManyField('Producto', verbose_name='Los productos del usuario') # Para relacionar con la clase producto(un usuario puede tener uno o mas productos "ManyToMany").


STATUS_CHOICES = ( # Se le pasa al parametro "estado"
    ('L', 'Leido'),
    ('N', 'No leido'),
    ('E', 'Error'),
    ('A', 'Aceptado'),
    
    
)


class Web(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField()
    data = models.DateField()
    valoracion = models.IntegerField()
    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE) # Para que este relacionado y si se borra el usuario se borra esta clase (relacion OneToOne uno a uno).
    estado = models.CharField(choices=STATUS_CHOICES, max_length=1)
    
    def tiempoPosteo(self):
        if self.data < datetime.date(2022, 7, 4):
            return 'Posteado despues de la semana'
        else:
            return 'Posteado antes de la semana'
            
    

class Producto(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True) # Es de clave primaria, no se puede repetir este campo.
    precio = models.IntegerField(max_length=20)
    estado = models.BooleanField(default=False)
    anio = models.IntegerField(max_length=10)
    
    
    @property
    def nombreCompleto(self):
        return f'El nombre completo de tu producto es: {self.nombre}'
    
    def __str__(self):
        return self.nombre
        
        
    
    
    
    
    
    
    
    
    
    
