from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from miWeb.forms import Registro
from django import forms
from django.views import View
from productos.models import Product

def index(request):
    product = Product.objects.all() # Mi variable product va a obtener todos los productos.
    return render(request, "index.html", {
        "title": "Productos",
        "productos": product
          
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(username=username, password=password)
        if usuario:
            login(request,usuario)
            messages.success(request,f'Bievenido {usuario.username}')
            return redirect("index")
        else:
            messages.error(request,'Datos invalidos')
        
        
    return render(request, "usuarios/login.html", {})


def salir(request):
    logout(request)
    messages.success(request, 'Sesion cerrada con exito')
    return redirect('login')


def registro(request):
    form = Registro(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        
        
        usuario = form.save()
        
        if usuario:
            login(request,usuario)
            messages.success(request, 'Enhorabuena registro exitoso!')
            return redirect("index")
        
        
    return render(request, 'usuarios/registro.html',{
        'form': form,
    })

def bienvenido(request):
    return HttpResponse('Bienvenido al curso')

def despedida(request):
    return HttpResponse('Hasta luego')
    

class MyClase(View):
    def get(self, request): #Con self accedo a atributos de una clase.
        return HttpResponse('Hola desde mi vista basada en clases')
     
    
    