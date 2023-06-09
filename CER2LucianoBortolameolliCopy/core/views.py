from django.shortcuts import render
from .models import Comunicado


# Create your views here.


def PagHomeIndex(request):
    return render(request, "core/home.html")



def ListaComunicados(request):
    #obtener Columnas de comunicado desde el Modelo
    Columnas= Comunicado.objects.all()

    #Definir contenido en columnas
    DatosCom={
        'inicio': Columnas,
    }

    #cargar listado DatosCom en request (envia el diccionario al template home)

    return render(request, 'core/home.html',DatosCom)


      