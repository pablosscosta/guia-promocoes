from rest_framework import routers
from .views import CategoryViewSet, EstablishmentViewSet, PromotionViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'establishments', EstablishmentViewSet)
router.register(r'promotions', PromotionViewSet)
urlpatterns = router.urls