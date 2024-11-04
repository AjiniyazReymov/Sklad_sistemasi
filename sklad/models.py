from django.utils import timezone

from django.db import models



class Material(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Warehouse(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    created_time = models.DateTimeField(default=timezone.now,)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.material_id}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6, blank=True, unique=True)
    created_time = models.DateTimeField(default=timezone.now,)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='materials')
    qty = models.IntegerField()
    created_time = models.DateTimeField(default=timezone.now,)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id}"
