# Generated by Django 3.2.23 on 2024-01-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_paciente_correo_verificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='contactos',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
