# Generated by Django 4.2 on 2023-04-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='id',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='numero_reserva',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]