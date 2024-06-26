"""
URL configuration for agendamento_refeicoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cadastros.views import LocalidadesListView, LocalidadesCreateView, LocalidadesUpdateView, LocalidadesDeleteView

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', LocalidadesListView.as_view(), name="localidades_list"),
    path('create', LocalidadesCreateView.as_view(), name="localidades_create"),
    path('update/<int:pk>', LocalidadesUpdateView.as_view(), name="localidades_update"),
    path('delete/<int:pk>', LocalidadesDeleteView.as_view(), name="localidades_delete"),
]

# Admin Site Config
admin.sites.AdminSite.site_header = 'Sistema de Agendamento de Refeições'