# Generated by Django 4.1.6 on 2023-08-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='pacientes_foto_perfil/'),
        ),
    ]
