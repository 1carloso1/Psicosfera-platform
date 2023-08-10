# Generated by Django 4.1.6 on 2023-08-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apaterno', models.CharField(max_length=120)),
                ('amaterno', models.CharField(max_length=120)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('ocupacion', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('antecedentes_medicos', models.TextField(blank=True)),
                ('diagnostico', models.TextField(blank=True)),
                ('tratamiento', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]