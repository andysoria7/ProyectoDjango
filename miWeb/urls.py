"""miWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos.views import ProductView
from .import views
from . views import MyClase
from django.urls import include
from django.conf.urls.static import static # Para las imagenes
from django.conf import settings # Para las imagenes

urlpatterns = [
    path('bienvenido/', views.bienvenido, name='bienvenido'), # Vista basada en funcion.
    path('clases/',MyClase.as_view(), name='clases'), #MyClase.as_view lo que hace es llamar a esa clase o darle un alias, vista basada en clases.
    path('despedida/', views.despedida, name='despedida'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/salir', views.salir, name="salir"),
    path('usuarios/login',views.login_view, name="login"),
    path("", ProductView.as_view(), name="index"), #Vista basada en clases desde productos.
    path('productos/', include('productos.urls') ), #Vista basada en clases con include() desde productos.
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
