# Generated by Django 3.1.2 on 2021-01-22 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0002_pelicula_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='genero',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelicula.genero'),
        ),
    ]
