from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Localidades

#FBV - Function Based Views
# def localidade_list(request):
#     localidades = Localidades.objects.all()
#     return render(request, "cadastros/localidades_list.html", {"localidades": localidades})

#CBV - Class Based Views
class LocalidadesListView(ListView):
    model = Localidades

class LocalidadesCreateView(CreateView):
    model = Localidades
    fields = ["localidade"]
    success_url = reverse_lazy("localidades_list")

class LocalidadesUpdateView(UpdateView):
    model = Localidades
    fields = ["localidade"]
    success_url = reverse_lazy("localidades_list")

class LocalidadesDeleteView(DeleteView):
    model = Localidades
    success_url = reverse_lazy("localidades_list")