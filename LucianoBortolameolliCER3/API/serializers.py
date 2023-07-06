from rest_framework import serializers
from core.models import Maquina,Herramienta

class Serializer_Maquina(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'


class Serializer_Herramienta(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = '__all__'