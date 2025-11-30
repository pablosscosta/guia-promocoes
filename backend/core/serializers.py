from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Establishment, Promotion
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

# Serializer para registrar novos usuários
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[("cliente", "Cliente"), ("estabelecimento", "Estabelecimento")])
    establishment = serializers.DictField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'establishment']

    def validate(self, attrs):
        role = attrs.get("role")
        establishment = attrs.get("establishment")

        if role == "estabelecimento" and not establishment:
            raise serializers.ValidationError("Dados do estabelecimento são obrigatórios para role 'estabelecimento'.")
        return attrs

    def create(self, validated_data):
        role = validated_data.get("role")
        establishment_data = validated_data.pop("establishment", None)

        # cria o usuário
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=role
        )

        # se for estabelecimento, cria o estabelecimento vinculado
        if role == "estabelecimento" and establishment_data:
            est = Establishment.objects.create(
                owner=user,
                name=establishment_data.get("name"),
                address=establishment_data.get("address"),
                phone_number=establishment_data.get("phone_number"),
            )
            if "categories" in establishment_data:
                est.categories.set(establishment_data["categories"])

        return user


# Serializer para categorias de estabelecimentos
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Serializer para estabelecimentos, incluindo categorias relacionadas
class EstablishmentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
         many=True, queryset=Category.objects.all(), source="categories", write_only=True
    )

    class Meta:
        model = Establishment
        fields = ['id', 'name', 'phone_number', 'address', 'categories', 'category_ids', 'owner']
        read_only_fields = ['owner']


# Serializer para promoções, incluindo nome do estabelecimento
class PromotionSerializer(serializers.ModelSerializer):
    establishment_name = serializers.CharField(source="establishment.name", read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'establishment', 'establishment_name', 'owner']
        read_only_fields = ['owner']


# Serializer para usuários, incluindo estabelecimentos e promoções relacionados
class UserSerializer(serializers.ModelSerializer):
    establishments = EstablishmentSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'establishments', 'promotions']


# Serializer customizado para login JWT, adicionando o campo 'role' do usuário

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = getattr(self.user, 'role', None)
        return data

# Serializer que retorna as informações do usuário
class MeDetailsSerializer(serializers.ModelSerializer):
    establishment = serializers.SerializerMethodField()
    promotions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "role", "establishment", "promotions"]

    def get_establishment(self, user):
        est = user.establishments.first()  # assume apenas 1
        if not est:
            return None
        return {
            "id": est.id,
            "name": est.name,
            "address": est.address,
            "phone_number": est.phone_number,
            "categories": list(est.categories.values_list("id", flat=True))
        }

    def get_promotions(self, user):
        est = user.establishments.first()
        if not est:
            return []
        promos = Promotion.objects.filter(establishment=est).values("id", "title", "description")
        return list(promos)