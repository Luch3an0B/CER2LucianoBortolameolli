from django.db import models


#from django.contrib.admin

from django.forms import fields

# Create your models here.



#ELEMENTOS BACK-END


class categoria(models.Model):
    Nombre_Categ= models.CharField(max_length=87,primary_key=True)
    Desc_Categ= models.CharField(max_length=434)

    def __str__(self):
        return self.Nombre_Categ
    #referenciar categoria con nombre



class Comunicado(models.Model):     #instancia de comunicado
    ID_Correl_Com=models.CharField(max_length=5,primary_key=True)
    #primary key correlativo
    Categ_Com=models.ForeignKey(categoria, on_delete=models.CASCADE)
    #foreign key categoria
    Titulo_Com=models.CharField(max_length=87)
    Mensaje_Com=models.CharField(max_length=434)

    Fecha_Env_Com=models.DateTimeField(auto_now_add=True)
    Fecha_Mod_Com=models.DateTimeField(auto_now=True)

    #lista de opciones curso para Choice_Com
    Lista_Curso= [ #lista de "niveles"
    ("C_Gen","General"),
    ("C_Pre","Preescolar"),
    ("C_Bas","Basica"),
    ("C_Med","Media")
    ]


    Curso_Choice_Com=models.CharField(choices=Lista_Curso, max_length=20, default="C_Gen")
    #Campo Choices para especificar a que curso dirigir comunicado
    

    def __str__(self):
        return self.Titulo_Com
    #referenciar categoria con titulo










#ELEMENTOS FRONT-END




#class user_trabajador():           
    #GRUPO USUARIOS Trabajadores hecho en admin

 #   Username_Trab=User.USERNAME_FIELD
    
    #models.CharField(max_length=30,primary_key=True)
  #  Password_Trab=models.CharField(max_length=90,unique=True)
   # Email_Trab=models.EmailField(unique=True)

    #def __str__(self):
     #   return self.Username_Trab    
    #referenciar usuario con apodo