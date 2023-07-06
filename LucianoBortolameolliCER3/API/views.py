from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Serializer_Herramienta,Serializer_Maquina
from core.models import Herramienta, Maquina

# Create your views here.

class Herramienta_ViewSet(viewsets.ModelViewSet):
    queryset= Herramienta.objects.all()
    serializer_class= Serializer_Herramienta

class Maquina_ViewSet(viewsets.ModelViewSet):
    queryset= Maquina.objects.all()
    serializer_class= Serializer_Maquina