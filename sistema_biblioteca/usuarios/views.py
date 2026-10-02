from django.shortcuts import render
from .models import usuarios

def listar_usuarios(request):
    lista_usuarios = usuarios.objects.all().order_by("nome")
    return render(request, "usuarios.html", {"usuarios": lista_usuarios})
