from rest_framework import routers
from .views import ProdutoViewSet, VendedorViewSet, CarrinhoViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet)
router.register('vendedores', VendedorViewSet)
router.register('clientes', ClienteViewSet)
router.register('carrinhos', CarrinhoViewSet)

urlpatterns = router.urls
