from rest_framework import serializers
from .models import Produto, Vendedor, Carrinho

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)
    vendedor = VendedorSerializer()
    class Meta:
        model = Carrinho
        fields = '__all__'

    def create(self, validated_data):
        #desestruturando payload
        produtos_data = validated_data.pop('produtos', [])
        vendedor_data = validated_data.pop('vendedor')
        #criando instancia de vendedor ou pegando instancia
        vendedor, created = Vendedor.objects.get_or_create(**vendedor_data)
        #criando o carrinho
        carrinho = Carrinho.objects.create(vendedor= vendedor)
        #criando instancia dos produtos que foram passados no payload e fazendo relacionamento com o carrinho
        for elem in produtos_data:
            produto, created = Produto.objects.get_or_create(**elem)
            produto.carrinho.add(carrinho)
        
        carrinho.save()
        return carrinho
