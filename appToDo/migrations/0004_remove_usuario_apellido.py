# Generated by Django 4.2.4 on 2023-08-20 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0003_tarea_titulo_alter_tarea_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
    ]