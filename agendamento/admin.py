from django.contrib import admin

from .models import Utilizadores, Reserva

class UtilizadoresAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'email', 'localidade')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'data_reserva', 'localidade_reserva', 'opcao_refeicao','numero_reserva')

admin.site.register(Utilizadores, UtilizadoresAdmin)
admin.site.register(Reserva, ReservaAdmin)
