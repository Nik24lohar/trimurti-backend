from .models import Product , Card , selectedProduct
from rest_framework import serializers

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CardSerializer (serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
class selectProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = selectedProduct
        fields = '__all__'