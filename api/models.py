from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255);
    preco = models.FloatField();

    def __str__(self):
        return f'produto {self.nome} - R${self.preco}.'