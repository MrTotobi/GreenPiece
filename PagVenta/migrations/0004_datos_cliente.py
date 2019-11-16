# Generated by Django 2.2.5 on 2019-11-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagVenta', '0003_auto_20191104_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=70)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono_contacto', models.CharField(max_length=12)),
                ('region', models.TextField()),
                ('comuna', models.TextField()),
                ('direccion', models.TextField()),
                ('vivienda', models.TextField()),
            ],
        ),
    ]
