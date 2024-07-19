from django.shortcuts import render
from datetime import datetime

def index(request):
    
    lista_usuarios = [
        {"nome": "Francisco", "Idade": 25},
        {"nome": "Willian", "Idade": 80},
        {"nome": "Afton", "Idade": 30},
        {"nome": "Scott", "Idade": 25},
        {"nome": "Cawton", "Idade": 396},
    ]
    context = {
        "usuarios": lista_usuarios
    }
    return render(request, "index.html", context)