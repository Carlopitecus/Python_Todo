# Generated by Django 4.2.4 on 2023-09-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0009_alter_tarea_categoria_alter_tarea_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
