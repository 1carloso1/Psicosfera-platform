# Generated by Django 4.1.6 on 2023-09-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0012_remove_psicologo_amaterno_remove_psicologo_apaterno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psicologo',
            name='edad',
            field=models.PositiveIntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='psicologo',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
