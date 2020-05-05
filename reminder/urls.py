"""reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from notas.views import NotasCreateView, NotasListView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='raiz'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    #notas
    path('notas/', TemplateView.as_view(template_name='misnotas.html'), name='notas'),
    path('notas/list/', NotasListView, name='list_notas'),
    path('notas/create/', NotasCreateView, name='create_notas'),
    path('notificaciones/', TemplateView.as_view(template_name='misnotificaciones.html'), name='notificaciones'),
    path('estadisticas/', TemplateView.as_view(template_name='estadisticas.html'), name='estadisticas'),
]
