from rest_framework import serializers
from .models import Produto, Vendedor, Carrinho, Cliente


class Vendas_carrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    vendas = serializers.SerializerMethodField()

    class Meta:
        model = Vendedor
        fields = '__all__'

    def get_vendas(self, obj):
        vendas_query = Carrinho.objects.filter(vendedor=obj)
        res = obj.__dict__
        print(f'INSTANCE => {obj}')
        print(f'QUERY => {res}')
        print(f'VENDAS => {vendas_query}')
        return Vendas_carrinhoSerializer(vendas_query, many=True).data


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)
    vendedor = VendedorSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Carrinho
        fields = '__all__'

    def create(self, validated_data):
        # desestruturando payload
        produtos_data = validated_data.pop('produtos', [])
        vendedor_data = validated_data.pop('vendedor')
        cliente_data = validated_data.pop('cliente')
        # criando instancia de vendedor ou pegando instancia
        vendedor, v_created = Vendedor.objects.get_or_create(**vendedor_data)
        cliente, c_created = Cliente.objects.get_or_create(**cliente_data)
        # criando o carrinho
        carrinho = Carrinho.objects.create(vendedor=vendedor, cliente=cliente)
        # criando instancia dos produtos que foram passados no payload e fazendo relacionamento com o carrinho
        for elem in produtos_data:
            produto, created = Produto.objects.get_or_create(**elem)
            produto.carrinho.add(carrinho)

        carrinho.save()
        return carrinho
