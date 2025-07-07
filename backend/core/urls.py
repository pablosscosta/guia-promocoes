from rest_framework import routers
from .views import EstablishmentViewSet, PromotionViewSet

router = routers.DefaultRouter()
router.register(r'establishments', EstablishmentViewSet)
router.register(r'promotions', PromotionViewSet)
urlpatterns = router.urls