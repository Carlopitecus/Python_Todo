# Generated by Django 4.2.4 on 2023-09-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0011_alter_tarea_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareacompletada',
            name='estado',
            field=models.CharField(default='Completada', max_length=150),
            preserve_default=False,
        ),
    ]