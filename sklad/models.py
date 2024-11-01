from django.db import models
from rest_framework.response import Response


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Warehouse(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return f"{self.material_id}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6, blank=True, unique=True)

    def __str__(self):
        return f"{self.name}"

class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return f"{self.product_id}"

class Shirt(ProductMaterial, models.Model):
    fabric_required = models.FloatField(default=0.8)  # м ткани на 1 рубашку
    buttons_required = models.IntegerField(default=5)  # количество пуговиц на 1 рубашку
    thread_required = models.FloatField(default=10)  # м ниток на 1 рубашку

    def __str__(self):
        return f"Shirt requirements: {self.fabric_required}m fabric, {self.buttons_required} buttons, {self.thread_required}m thread"