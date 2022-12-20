from django.shortcuts import render
from .models import Captura

def capturas(request, code_user):
    titulo = "Capturas de informação"
    captura = Captura.objects.filter(code_user=code_user)
    return render(request, 'capturas.html',
                  {'titulo': titulo, 'capturas': captura, 'code_user': code_user})



