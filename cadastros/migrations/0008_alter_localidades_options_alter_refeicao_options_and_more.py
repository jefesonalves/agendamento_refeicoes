# Generated by Django 5.0.4 on 2024-04-19 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_utilizadores_refeicao_utilizador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localidades',
            options={'verbose_name_plural': 'Localidades'},
        ),
        migrations.AlterModelOptions(
            name='refeicao',
            options={'verbose_name_plural': 'Refeição'},
        ),
        migrations.AlterModelOptions(
            name='utilizadores',
            options={'verbose_name_plural': 'Utilizadores'},
        ),
    ]
