from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Establishment, Promotion

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EstablishmentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
         many=True, queryset=Category.objects.all(), source="categories", write_only=True
    )

    class Meta:
        model = Establishment
        fields = ['id', 'name', 'phone_number', 'address', 'categories', 'category_ids', 'owner']
        read_only_fields = ['owner']


class PromotionSerializer(serializers.ModelSerializer):
    establishment_name = serializers.CharField(source="establishment.name", read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'establishment', 'establishment_name', 'owner']
        read_only_fields = ['owner']


class UserSerializer(serializers.ModelSerializer):
    establishments = EstablishmentSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'establishments', 'promotions']
