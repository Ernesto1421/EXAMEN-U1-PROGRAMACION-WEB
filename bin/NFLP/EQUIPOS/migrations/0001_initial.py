# Generated by Django 2.1.1 on 2018-09-08 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ESTADIOS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Colonia', models.CharField(max_length=100)),
                ('Patrocinador', models.CharField(max_length=100)),
                ('Coach', models.CharField(max_length=100)),
                ('Estadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Estadio_de_equipo', to='ESTADIOS.Estadio')),
            ],
        ),
    ]
