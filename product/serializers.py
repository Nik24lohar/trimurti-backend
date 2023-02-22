from .models import Product , Card
from rest_framework import serializers

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CardSerializer (serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'