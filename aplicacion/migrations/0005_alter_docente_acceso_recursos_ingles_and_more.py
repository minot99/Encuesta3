# Generated by Django 4.2.11 on 2024-04-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_director_actividades_externas_centro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='acceso_recursos_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='ano_certificacion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='apellido',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cantidad_senalizaciones_aula',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cedula',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='docente',
            name='certificacion_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='correo_institucional',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cursos_internacionales_ingles',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cursos_nacionales_ingles',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docente',
            name='dispuesto_renovar_certificacion',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='experiencia_anos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='frecuencia_actividades_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='frecuencia_uso_recursos_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='habla_ingles_en_clase',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='incentiva_hablar_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='interactua_directivos_ingles',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='interactua_docentes_ingles',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='interactua_estudiantes_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='interactua_padres_ingles',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nivel_actual',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nivel_ingles_docente',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nombre_titulacion',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='docente',
            name='porcentaje_interaccion_estudiantes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='porcentaje_tiempo_ingles',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='sector_experiencia',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='senalizaciones_aula_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='telefono_oficina',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='telefono_personal',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='tiempo_dialogo_ingles',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='docente',
            name='titulo_ensenanza_ingles',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='titulos_formales_ingles',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docente',
            name='vencimiento_certificacion',
            field=models.CharField(default='', max_length=10),
        ),
    ]