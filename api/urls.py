from rest_framework import routers
from .views import ProdutoViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet)

urlpatterns = router.urls