from django.urls import path
from .views import listar_emprestimos

urlpatterns = [
    path('', listar_emprestimos),
]