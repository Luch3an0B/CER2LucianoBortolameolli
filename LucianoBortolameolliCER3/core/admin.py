from django.contrib import admin
from core.models import Maquina, Herramienta

# Register your models here.

class registro_Maquina (admin.ModelAdmin):
    pass
admin.site.register (Maquina,registro_Maquina)

class registro_Herramienta (admin.ModelAdmin):
    pass
admin.site.register (Herramienta,registro_Herramienta)