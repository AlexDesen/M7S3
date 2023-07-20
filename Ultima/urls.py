"""
URL configuration for Ultima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from basic.views import inicio
from basic.views import modelo
# from basic.views import reserva
# from reservando.views import criar_reserva
from eventos.views import eventos



urlpatterns = [
    path('',modelo),
    path('inicio/',inicio,name='inicio'),
    # Dessa forma é passada o id para a função eventos na views
    # O parâmetro "nome=" nomeia a nossa url, neste caso "eventos" 
    path('eventos/<id>/',eventos,name='eventos'), 
    path('reserva/',include('basic.url',namespace='reservas')),
    path('criar/',include('reservando.url',namespace='reserva')),
    # path('reservando/',include('reservando.url',namespace='reservando')),
    path("admin/", admin.site.urls),
    path('api_auth/',include('rest_framework.urls')),
    # o rest_api.url - é o endereço onde se encontra o restante da url que 
    # esta no módulo rest_api no arquivo url.py 
    # ficando assim: http://127.0.0.1:8000/api/categoria/
     path('api/', include('rest_api.url', namespace='api')), 
    path('apiProduto/',include('resgistroProduto.url',namespace='apiProduto'))  
   
 
]
