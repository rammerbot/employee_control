# Generated by Django 5.0.1 on 2024-01-13 09:55

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch', models.CharField(max_length=20, verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='EntryHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.branch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
            ],
            options={
                'verbose_name': 'Hora de Entrada',
                'verbose_name_plural': 'Horas de Entrada',
            },
        ),
        migrations.CreateModel(
            name='ExitHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.branch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
            ],
            options={
                'verbose_name': 'Hora de Salida',
                'verbose_name_plural': 'Horas de Salida',
            },
        ),
        migrations.CreateModel(
            name='LunchEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.branch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
            ],
            options={
                'verbose_name': 'Fin de Almuerzo',
                'verbose_name_plural': 'Fin de Almuerzo',
            },
        ),
        migrations.CreateModel(
            name='LunchStart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.branch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
            ],
            options={
                'verbose_name': 'Inicio de almuerzo',
                'verbose_name_plural': 'Inicios de Almuerzo',
            },
        ),
    ]
