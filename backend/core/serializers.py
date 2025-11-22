from rest_framework import serializers
from .models import Category, Establishment, Promotion

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
        fields = ['id', 'name', 'phone_number', 'address', 'categories', 'category_ids']


class PromotionSerializer(serializers.ModelSerializer):
    establishment_name = serializers.CharField(source="establishment.name", read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'establishment', 'establishment_name']
