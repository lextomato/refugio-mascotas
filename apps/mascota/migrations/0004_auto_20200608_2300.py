# Generated by Django 3.0.5 on 2020-06-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20200516_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(upload_to='frontend/dist/static/media/Mascotas/'),
        ),
    ]
