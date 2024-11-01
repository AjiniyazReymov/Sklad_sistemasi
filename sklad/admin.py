from django.contrib import admin
from .models import Material, Warehouse, Product, ProductMaterial

class MaterailModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_id', 'remainder', 'price']

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']

class ProductMaterialModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'material_id', 'qty']

admin.site.register(Material, MaterailModelAdmin)
admin.site.register(Warehouse, WarehouseModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductMaterial, ProductMaterialModelAdmin)