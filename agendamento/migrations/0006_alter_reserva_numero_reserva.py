# Generated by Django 4.2 on 2023-04-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0005_remove_reserva_id_alter_reserva_numero_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='numero_reserva',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
