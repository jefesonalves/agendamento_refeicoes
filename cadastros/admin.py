from django.contrib import admin

from .models import Localidades, Refeicao, Utilizadores

class LocalidadesAdmin(admin.ModelAdmin):
    list_display = ['localidade']

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ['refeicao']

class UtilizadoresAdmin(admin.ModelAdmin):
    list_display = ['matricula_utilizador', 'nome_utilizador', 'email_utilizador']

admin.site.register(Localidades, LocalidadesAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Utilizadores, UtilizadoresAdmin)
