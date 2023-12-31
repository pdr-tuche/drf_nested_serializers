from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()

    def __str__(self):
        return f'produto {self.nome} - R${self.preco}.'


class Vendedor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    vendedor = models.ForeignKey(
        Vendedor, related_name='carrinho', on_delete=models.DO_NOTHING)
    produtos = models.ManyToManyField(Produto, related_name='carrinho')
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'carrinho: {self.id}, vendedor: {self.vendedor}'
