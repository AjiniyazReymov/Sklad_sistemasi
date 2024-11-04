from rest_framework import serializers
from .models import Material, Warehouse, Product, ProductMaterial

class WarehouseSerializer(serializers.ModelSerializer):
    material_name = serializers.SerializerMethodField()

    class Meta:
        model = Warehouse
        fields = ['id', 'material_name', 'remainder']

    def get_material_name(self, obj):
        return obj.material.name if obj.material else None

class ProductMaterialSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()

    class Meta:
        model = ProductMaterial
        fields = ['id', 'product_name', 'code', 'qty']

    def get_product_name(self, obj):
        return obj.product.name if obj.product else None

    def get_product_code(self, obj):
        return obj.product.code if obj.product else None
