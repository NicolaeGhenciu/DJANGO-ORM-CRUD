# Generated by Django 4.1.3 on 2023-01-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_rename_description_libro_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
