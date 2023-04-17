# Generated by Django 4.2 on 2023-04-17 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_rename_utilizador_utilizadores_nome_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('numero_reserva', models.PositiveIntegerField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamento.utilizadores', unique=True)),
            ],
        ),
    ]
