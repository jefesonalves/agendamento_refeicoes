from django.db import models
from multiselectfield import MultiSelectField


class Utilizadores(models.Model):
    LOCALIDADES = (
        ('areias', 'Areias'),
        ('cajazeiras', 'Cajazeiras'),
    )

    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=30, null=False, default="")
    email = models.EmailField(max_length=254, unique=True, default="")
    localidade = models.CharField(max_length=100, choices=LOCALIDADES, default="")

    class Meta:
        verbose_name = 'Utilizadores'
        verbose_name_plural = 'Utilizadores'

    def __str__(self):
            return f'{self.matricula}'

class Reserva(models.Model):
    LOCALIDADES_RESERVA = (
        ('areias', 'Areias'),
        ('cajazeiras', 'Cajazeiras'),
    )

    OPCOES_REFEICOES = (
        ('lanche_manha', 'Lanche da Manhã'),
        ('almoco', 'Almoço'),
        ('lanche_tarde', 'Lanche da Tarde'),
        ('jantar', 'Jantar'),
    )

    matricula = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    numero_reserva = models.AutoField(primary_key=True)
    localidade_reserva = models.CharField(max_length=100, choices=LOCALIDADES_RESERVA, default="")
    opcao_refeicao = MultiSelectField(max_length=100, choices=OPCOES_REFEICOES, default="")

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reserva'