from rest_framework import serializers
from .models import Material, Warehouse, Product, ProductMaterial

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']

class WarehouSeerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'material_id', 'remainder', 'price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code']

class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = ['id', 'product_id', 'material_id', 'qty']