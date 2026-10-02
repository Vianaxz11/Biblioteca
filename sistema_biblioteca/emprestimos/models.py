from django.db import models

class Emprestimo(models.Model):
    livro = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.livro

# Create your models here.
