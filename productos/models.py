from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() #Textarea
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    create_at = models.DateField(auto_now_add=True) # Se va a generar automaticamente la fecha de cuando se cree si esta en True.
    slug = models.SlugField(null=False, blank=False, unique=True) # Especificamos que no sea nulo, no pueda estar en blanco y sea unico.
    image = models.ImageField(upload_to='productos/', null= False, blank=False)
    
    def __str__(self):
        return self.title # Retornara por titulo lo que se agregue en el admin de Django (base de datos).
    
    # def save(self, *args, **kwargs ): # le pasamos el self, los argumentos y el diccionario de argumentos.
    #     self.slug = slugify(self.title)
    #     super(Product,self).save(*args, **kwargs)
    
def set_slug(sender, instance, *args, **kwargs): # los * son los diccionarios de argumentos.
    if instance.title and not instance.slug: # Si no tenemos un slug entonces vamos a generarlo.
        slug = slugify(instance.title) # Entonces vamos a generarlo.
        
        while Product.objects.filter(slug=slug).exists(): # Si existe hacemos un while filtrado a traves de slug.
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])) # Se genera a partir del titulo y a partir de una libreria llamada uuid.
            
        instance.slug = slug
            
        
pre_save.connect(set_slug,sender=Product)


    
    
        
    
