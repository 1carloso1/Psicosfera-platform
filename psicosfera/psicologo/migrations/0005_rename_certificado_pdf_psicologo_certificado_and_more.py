# Generated by Django 4.1.6 on 2023-08-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0004_consultorio_alter_psicologo_especialidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psicologo',
            old_name='certificado_pdf',
            new_name='certificado',
        ),
        migrations.RemoveField(
            model_name='psicologo',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='psicologo',
            name='anio_obtencion',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='curriculum',
            field=models.FileField(blank=True, null=True, upload_to='curriculum_psicologo/'),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='enlace_facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='enlace_instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='enlace_linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='enlace_pagina_web',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='institucion_otorgamiento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='psicologo',
            name='metodo_pago',
            field=models.CharField(blank=True, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de Crédito/Débito'), ('transferencia', 'Transferencia Bancaria'), ('paypal', 'PayPal')], max_length=100, null=True),
        ),
    ]
