from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin): # Herencia.
    fields = ('title', 'description', 'price', 'image') # Aqui le pasamos los campos.
    list_display = ('__str__', 'slug', 'create_at') # Para visualizarlos.
    




admin.site.register(Product, ProductAdmin) # Registramos producto.