from tempfile import template

from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import context, loader

from .models import Usuario

# Create your views here.

def saludar(request):
    template = loader.get_template('saludar.html') 
    return HttpResponse(template.render())


def usuarios(request):
    template = loader.get_template('usuarios.html')
    usuarios = Usuario.objects.all().values()
    context = {
        'usuarios_html': usuarios
    }

    return HttpResponse(template.render(context, request))


