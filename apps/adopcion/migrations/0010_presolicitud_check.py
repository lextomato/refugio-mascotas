# Generated by Django 3.0.5 on 2020-07-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0009_auto_20200706_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='presolicitud',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
