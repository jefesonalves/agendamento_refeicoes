from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Sistema de Agendamentos de Refeições na View")
