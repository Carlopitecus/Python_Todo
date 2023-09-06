# Generated by Django 4.2.4 on 2023-09-04 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0008_alter_tarea_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='categoria',
            field=models.CharField(max_length=150, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=150, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fechaTermino',
            field=models.DateField(verbose_name='Fecha de Termino'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.CreateModel(
            name='TareaCompletada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fechaCompletada', models.DateField()),
                ('categoria', models.CharField(max_length=150)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
