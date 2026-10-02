from django.shortcuts import render
from .models import Emprestimo

def listar_emprestimos(request):
    lista_emprestimos = Emprestimo.objects.all().order_by("-data_emprestimo")
    return render(request, "emprestimos.html", {"emprestimos": lista_emprestimos})

# Create your views here.
