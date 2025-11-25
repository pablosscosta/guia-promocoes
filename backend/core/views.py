from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly
from .models import Category, Establishment, Promotion
from .serializers import (
    RegisterSerializer,
    CategorySerializer,
    EstablishmentSerializer,
    PromotionSerializer,
    UserSerializer
)


# -----------------------------
# Registro de usuários
# -----------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuário criado com sucesso"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# Categorias
# -----------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# -----------------------------
# Estabelecimentos
# -----------------------------
class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -----------------------------
# Promoções
# -----------------------------
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -----------------------------
# Perfil do usuário (detalhado)
# -----------------------------
class MeDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        establishments = Establishment.objects.filter(owner=user)
        promotions = Promotion.objects.filter(owner=user)

        establishments_data = EstablishmentSerializer(establishments, many=True).data
        promotions_data = PromotionSerializer(promotions, many=True).data

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "establishments": establishments_data,
            "promotions": promotions_data,
        })


# -----------------------------
# Perfil do usuário (resumido)
# -----------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    establishments_count = Establishment.objects.filter(owner=user).count()
    promotions_count = Promotion.objects.filter(owner=user).count()

    return Response({
        "id": user.id,
        "username": user.username,
        "establishments_count": establishments_count,
        "promotions_count": promotions_count,
    })
