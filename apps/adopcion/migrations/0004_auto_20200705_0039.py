# Generated by Django 3.0.5 on 2020-07-05 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_presolicitud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presolicitud',
            name='mascota',
        ),
        migrations.RemoveField(
            model_name='presolicitud',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='presolicitud',
            name='solicitud',
        ),
    ]
