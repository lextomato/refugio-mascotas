# Generated by Django 3.0.5 on 2020-05-14 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mascotas', models.IntegerField()),
                ('razones', models.TextField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adopcion.Persona')),
            ],
        ),
    ]
