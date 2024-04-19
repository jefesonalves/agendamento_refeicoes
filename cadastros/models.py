from django.db import models

class Localidades(models.Model):
    localidade = models.CharField(max_length=100, default="", verbose_name='Localidade')    

    class Meta:
        verbose_name_plural = 'Localidades'

    def __str__(self):
            return f'{self.localidade}'

class Refeicao(models.Model):
    refeicao = models.CharField(max_length=100, default="", verbose_name='Refeição')    

    class Meta:
        verbose_name_plural = 'Refeição'

    def __str__(self):
            return f'{self.refeicao}'

class Utilizadores(models.Model):
    matricula_utilizador = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    nome_utilizador = models.CharField(max_length=50, null=False, default="", verbose_name='Nome')
    email_utilizador = models.EmailField(max_length=254, unique=True, default="", verbose_name='e-mail')
    localidade_utilizador = models.ForeignKey(Localidades, on_delete=models.CASCADE, verbose_name='Localidade')
    refeicao_utilizador = models.ManyToManyField(Refeicao, verbose_name='Refeições')

    class Meta:
        verbose_name_plural = 'Utilizadores'

    def __str__(self):
            return f'{self.matricula_utilizador}{self.nome_utilizador}{self.email_utilizador}{self.localidade_utilizador}'