# Generated by Django 4.2 on 2023-07-06 00:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id_etiqueta', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(9)])),
                ('marca_herramienta', models.CharField(max_length=16)),
                ('estado_herramienta', models.CharField(choices=[('Usando', 'En Uso'), ('Disponible', 'Disponible'), ('No_Disponible', 'Fuera de Servicio'), ('Reparando', 'En Reparacion')], default='Usando', max_length=25)),
                ('tipo_herramienta', models.CharField(choices=[('Paleta_Tool', 'Paleta'), ('Spatula_Tool', 'Espatula'), ('Frata_Tool', 'Frata'), ('Regla_Burbuja', 'Nivelador de Burbuja'), ('Rule', 'Regla'), ('Mazo_Tool', 'Mazo'), ('Flexometro', 'Cinta para Medir'), ('Pala_Square', 'Pala Cuadrada'), ('Pala_Circle', 'Pala_Redonda'), ('Martillo_Tool', 'Martillo'), ('Handsaw', 'Serrucho'), ('Saw', 'Sierra Electrica'), ('bucket', 'Balde'), ('manguera_tool', 'Manguera'), ('pick_tool', 'Pico'), ('wrench', 'Llave Inglesa')], default='Paleta_Tool', max_length=30)),
                ('precio_herramienta', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('placa_matricula', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Placa de Identificacion')),
                ('marca_maquina', models.CharField(max_length=16)),
                ('estado_maquina', models.CharField(choices=[('Usando', 'En Uso'), ('Disponible', 'Disponible'), ('No_Disponible', 'Fuera de Servicio'), ('Reparando', 'En Reparacion')], default='Usando', max_length=25)),
                ('tipo_maquina', models.CharField(choices=[('Maq_Cargador', 'Cargador'), ('Maq_Compactador', 'Compactador'), ('Drag_Line', 'Dragalina'), ('Maq_Excavator', 'Excavadora'), ('Dump_Rigid', 'Dumper Rigido'), ('Dump_Artiq', 'Dumper Articulado'), ('Drill', 'Taladro'), ('Maq_Manipulador', 'Manipulador de Materiales'), ('Perforer_Maq', 'Perforadora'), ('Generator_Maq', 'Generador'), ('Motor_Grade_Maq', 'Motonivelador'), ('Dozer_Blade', 'Hoja de Empuje'), ('Pipe_Layer', 'TiendeTubo')], default='Maq_Cargador', max_length=30)),
                ('precio_maq', models.IntegerField(max_length=9)),
            ],
        ),
    ]
