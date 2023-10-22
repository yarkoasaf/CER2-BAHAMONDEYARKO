# Generated by Django 4.2.6 on 2023-10-22 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('detalle', models.TextField(max_length=120)),
                ('detalle_corto', models.TextField(max_length=60)),
                ('tipo', models.CharField(choices=[('S', 'Suspensión de actividades'), ('C', 'Suspensión de clase'), ('T', 'Información')], max_length=1)),
                ('visible', models.BooleanField(default=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.entidad')),
            ],
        ),
    ]
