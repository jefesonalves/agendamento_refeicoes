from django.db import models

class Utilizadores(models.Model):
    LOCALIDADES = (
        ('areias', 'Areias'),
        ('cajazeiras', 'Cajazeiras'),
    )

    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=30, null=False, default="")
    email = models.EmailField(max_length=254, unique=True, default="")
    localidade = models.CharField(max_length=100, choices=LOCALIDADES, default="")

    def __str__(self):
            return f'{self.matricula}'

class Reserva(models.Model):
    matricula = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_now_add=True)
    numero_reserva = models.AutoField(primary_key=True)