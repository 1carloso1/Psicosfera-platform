# Generated by Django 4.1.6 on 2023-09-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0013_alter_psicologo_edad_alter_psicologo_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psicologo',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
    ]
