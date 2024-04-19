# Generated by Django 5.0.4 on 2024-04-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_alter_utilizadores_refeicao_utilizador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilizadores',
            name='refeicao_utilizador',
        ),
        migrations.AddField(
            model_name='utilizadores',
            name='refeicao_utilizador',
            field=models.ManyToManyField(to='cadastros.refeicao', verbose_name='Refeições'),
        ),
    ]
