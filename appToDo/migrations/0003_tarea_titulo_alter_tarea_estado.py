# Generated by Django 4.2.4 on 2023-08-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0002_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='algo', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=150),
        ),
    ]