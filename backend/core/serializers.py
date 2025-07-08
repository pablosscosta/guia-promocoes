from rest_framework import serializers
from .models import Category, Establishment, Promotion

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    establishment = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model= Promotion
        fields = '__all__'