# Generated by Django 4.2.1 on 2023-06-07 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_lunchentry_lunchend_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunchend',
            options={'verbose_name': 'Fin de Almuerzo', 'verbose_name_plural': 'Fin de Almuerzo'},
        ),
        migrations.AlterModelOptions(
            name='lunchstart',
            options={'verbose_name': 'Inicio de almuerzo', 'verbose_name_plural': 'Inicios de Almuerzo'},
        ),
    ]
