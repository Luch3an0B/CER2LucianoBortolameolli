from django.contrib import admin
from core.models import categoria, Comunicado #, user_trabajador

# Register your models here.

class registro_Comunicado (admin.ModelAdmin):
    pass
admin.site.register (Comunicado,registro_Comunicado)

class registro_Categoria(admin.ModelAdmin):
    pass
admin.site.register (categoria,registro_Categoria)

#class registro_Usuario (admin.ModelAdmin):
 #   pass
#admin.site.register (user_trabajador,registro_Usuario)