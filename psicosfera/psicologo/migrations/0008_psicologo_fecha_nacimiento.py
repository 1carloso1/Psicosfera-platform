# Generated by Django 4.1.6 on 2023-08-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0007_remove_consultorio_psicologo_psicologo_consultorio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='psicologo',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
