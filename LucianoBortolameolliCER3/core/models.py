from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db.models import F
from datetime import date

# Create your models here.


#class FixedLengthCharField(models.CharField):  
   #def __init__(self, *args, **kwargs):    
  #      kwargs['max_length'] = self.fixed_length   
#        super().__init__(*args, **kwargs)  

#    def deconstruct(self):     
 #       name, path, args, kwargs = super().deconstruct()   
 #      if 'max_length' in kwargs:  
  #         del kwargs['max_length']    
  #      return name, path, args, kwargs   

 #  def formfield(self, **kwargs):     
 #       defaults = {'max_length': self.fixed_length} 
 #       defaults.update(kwargs)                
 #       return super().formfield(**defaults)   

Lista_Estado= [
    ("Usando","En Uso"),
    ("Disponible","Disponible"),
    ("No_Disponible","Fuera de Servicio"),
    ("Reparando","En Reparacion")
]

Lista_Tipo_Maq=[
    ("Maq_Cargador","Cargador"),
    ("Maq_Compactador","Compactador"),
    ("Drag_Line","Dragalina"),
    ("Maq_Excavator","Excavadora"),
    ("Dump_Rigid","Dumper Rigido"),
    ("Dump_Artiq","Dumper Articulado"),
    ("Drill","Taladro"),
    ("Maq_Manipulador","Manipulador de Materiales"),
    ("Perforer_Maq","Perforadora"),
    ("Generator_Maq","Generador"),
    ("Motor_Grade_Maq","Motonivelador"),
    ("Dozer_Blade","Hoja de Empuje"),
    ("Pipe_Layer","TiendeTubo")
]

Lista_Tipo_Tool=[
    ("Paleta_Tool","Paleta"),
    ("Spatula_Tool","Espatula"),
    ("Frata_Tool","Frata"),
    ("Regla_Burbuja","Nivelador de Burbuja"),
    ("Rule","Regla"),
    ("Mazo_Tool","Mazo"),
    ("Flexometro","Cinta para Medir"),
    ("Pala_Square","Pala Cuadrada"),
    ("Pala_Circle","Pala_Redonda"),
    ("Martillo_Tool","Martillo"),
    ("Handsaw","Serrucho"),
    ("Saw","Sierra Electrica"),
    ("bucket","Balde"),
    ("manguera_tool","Manguera"),
    ("pick_tool","Pico"),
    ("wrench","Llave Inglesa")
]

class Maquina(models.Model):
    placa_matricula= models.CharField("Placa de Identificacion",primary_key=True, unique=True,max_length=6, validators=[MinLengthValidator(6)])
    
    #FixedLengthCharField(fixed_length=6,unique=True,primary_key=True)
    marca_maquina= models.CharField(max_length=16)
    estado_maquina= models.CharField(max_length=25, choices=Lista_Estado, default="Usando")
    tipo_maquina= models.CharField(max_length=30, choices=Lista_Tipo_Maq, default="Maq_Cargador")
    precio_maq= models.IntegerField(max_length=9)
    
    #oferta_maq= models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=1.0)

  #  precio_total_maquina= F(precio_maq)*F(oferta_maq)
   # limite_oferta_maq= models.DateField(default="07/12/2023")

    #if date.today() >= limite_oferta_maq.date():
      #  oferta_maq=1.0


class Herramienta(models.Model):
    id_etiqueta= models.CharField(primary_key=True, unique=True, max_length=9, validators=[MinLengthValidator(9)])
    
    #FixedLengthCharField(fixed_length=9,unique=True,primary_key=True)
    marca_herramienta= models.CharField(max_length=16)
    estado_herramienta= models.CharField(max_length=25, choices=Lista_Estado, default="Usando")
    tipo_herramienta= models.CharField(max_length=30, choices=Lista_Tipo_Tool, default="Paleta_Tool")
    precio_herramienta= models.IntegerField(max_length=9)
 
 #   oferta_herramienta= models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=1.0)

  #  precio_total_herramienta= F(precio_herramienta)*F(oferta_herramienta)
   # limite_oferta_herramienta= models.DateField()

    #if date.today() >= limite_oferta_herramienta:
    #    oferta_maq=1.0