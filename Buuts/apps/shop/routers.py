from rest_framework.routers import DefaultRouter
#
from .viewsets import (
    BrandViewSet,
    ModelViewSet,
    TaxViewSet,
    SizeViewSet,
    ProductViewSet,
)

router = DefaultRouter()

router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'models', ModelViewSet, basename='models')
router.register(r'taxs', TaxViewSet, basename='taxs')
router.register(r'sizes', SizeViewSet, basename='sizes')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls