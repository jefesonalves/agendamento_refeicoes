# Generated by Django 5.0.4 on 2024-04-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_refeicoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refeicao', models.CharField(default='', max_length=100, verbose_name='Refeição')),
            ],
            options={
                'verbose_name': 'Refeicao',
                'verbose_name_plural': 'Refeição',
            },
        ),
        migrations.DeleteModel(
            name='Refeicoes',
        ),
    ]
