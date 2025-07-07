from rest_framework import viewsets
from .models import Establishment, Promotion
from .serializers import EstablishmentSerializer, PromotionSerializer

# implementar a view category em outro momento. Não no MVP

class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer