# Generated by Django 5.0.4 on 2024-04-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidade', models.CharField(default='', max_length=100, verbose_name='Refeições')),
            ],
            options={
                'verbose_name': 'Refeicoes',
                'verbose_name_plural': 'Refeições',
            },
        ),
    ]