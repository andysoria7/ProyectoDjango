from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Product
# Create your views here.

class ProductView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id') # Ordena por id
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # lo que hace es yendo a buscar el contexto a nuestra clase superior.
        context ['productos'] = context['product_list'] # ya sea product_list o object_list, nos va a servir. Por defecto del class de models.py o de objects_list.
        
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detalle_producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #
        print(context)
        
        return context # siempre retornar para que muestre.
    
        
        


