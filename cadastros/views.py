from django.shortcuts import render
from django.views.generic import ListView

from .models import Localidades

#FBV - Function Based Views
# def localidade_list(request):
#     localidades = Localidades.objects.all()
#     return render(request, "cadastros/localidades_list.html", {"localidades": localidades})

#CBV - Class Based Views
class LocalidadesListView(ListView):
    model = Localidades