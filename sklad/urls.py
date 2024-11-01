from venv import create

from django.urls import path

from .views import ProductView

urlpatterns = [
    path('api/products/', ProductView.as_view(), name='product-list')
]