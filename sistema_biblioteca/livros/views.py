from django.shortcuts import render
from .models import livros

def listar_livros(request):
    lista_livros = livros.objects.all().order_by("titulo")
    return render(request, "livros.html", {"livros": lista_livros})

# Create your views here.
