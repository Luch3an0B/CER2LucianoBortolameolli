from django.shortcuts import render
from .models import Maquina, Herramienta

# Create your views here.



def vista_core(request):
    return render(request,'core/Home.html')

def vista_maquinas(request):

    lista_maquinas= Maquina.objects.all()


    datos_maquinas= {
        "Maquinas":lista_maquinas
    }
    return render(request,"core/Home.html",datos_maquinas)


def vista_herramientas(request):

    lista_herramientas= Herramienta.objects.all()


    datos_herramientas= {
        "Herramientas":lista_herramientas
    }
    return render(request,"core/Home.html",datos_herramientas)


def nueva_herramienta(request):
    if (request.POST):
        etiqueta = request.POST['id_herramienta']
        marca = request.POST['marca_herramienta']
        estado = request.POST['estado_herramienta']
        tipo= request.POST[' tipo_herramienta']
        Precio= int(request.POST['precio_herramienta'])

        #validaciones y lógica de negocio

        Tool = Herramienta(id_herramienta=etiqueta,marca_herramienta=marca,estado_herramienta=estado,tipo_herramienta=tipo,precio_herramienta=Precio)
        Tool.save()
        
    
    #obtener listado de herramientas desde el Modelo
    lista_herramientas= Herramienta.objects.all()

    #cargar listado en diccionario datos_herramientas
    datos_herramientas= {
        "Herramientas":lista_herramientas
    }
    
    #cargar diccionario datos en el request (Lo envía a template carreras.html)
   
    return render(request,"core/Home.html",datos_herramientas)



def nueva_maquina(request):
    if (request.POST):
        placa = request.POST['placa_matricula']
        marca = request.POST['marca_maquina']
        estado = request.POST['estado_maquina']
        tipo= request.POST[' tipo_maquina']
        Precio= int(request.POST['precio_maq'])

        #validaciones y lógica de negocio

        Maq = Maquina(placa_matricula=placa,marca_maquina=marca,estado_maquina=estado,tipo_maquina=tipo,precio_maq=Precio)
        Maq.save()
        
    
    #obtener listado de herramientas desde el Modelo
    lista_maquinas= Maquina.objects.all()

    #cargar listado en diccionario datos_herramientas
    datos_maquinas= {
        "Herramientas":lista_maquinas
    }
    
    #cargar diccionario datos en el request (Lo envía a template carreras.html)
   
    return render(request,"core/Home.html",datos_maquinas)


