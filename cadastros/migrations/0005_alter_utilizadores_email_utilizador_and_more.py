# Generated by Django 5.0.4 on 2024-04-18 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_utilizadores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizadores',
            name='email_utilizador',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='utilizadores',
            name='localidade_utilizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.localidades', verbose_name='Localidade'),
        ),
        migrations.AlterField(
            model_name='utilizadores',
            name='matricula_utilizador',
            field=models.CharField(max_length=20, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='utilizadores',
            name='nome_utilizador',
            field=models.CharField(default='', max_length=30, verbose_name='Nome'),
        ),
    ]