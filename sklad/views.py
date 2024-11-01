from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from sklad.models import Warehouse, Material, Product
from sklad.serializers import ProductSerializer, MaterialSerializer, WarehouSeerializer, ProductMaterialSerializer

class ProductView(APIView):

    def post(self, request):
        product_code = request.data.get("code")
        quantity = request.data.get("qty")

        if not product_code or not quantity:
            return Response({"error": "Code and quantity are required."}, status=status.HTTP_400_BAD_REQUEST)

        materials_check = self.check_materials_for_shirts(quantity)
        if materials_check['status'] == False:
            return Response(materials_check['message'], status=status.HTTP_400_BAD_REQUEST)

        return Response({
                "product_name": 'Koylak',
                "product_qty": quantity,
                "product_materials": [
                    {"warehouse_id": 1, "material_name": 'Mato', "qty": quantity, "price": 1500}]}, status=status.HTTP_201_CREATED)

    def shirt(self):
        fabric_required = 0.8
        buttons_required = 5
        thread_required = 10

        return {
            'fabric_required': fabric_required,
            'buttons_required': buttons_required,
            'thread_required': thread_required
        }

    def check_materials_for_shirts(self, quantity):
        shirt = self.shirt()
        total_fabric_needed = quantity * shirt['fabric_required']
        total_buttons_needed = quantity * shirt['buttons_required']
        total_thread_needed = quantity * shirt['thread_required']

        warehouse = Warehouse.objects.first()
        if not warehouse:
            return {'status': False, 'message': 'Warehouse not found.'}

        if (total_fabric_needed > warehouse.remainder and
            total_buttons_needed > warehouse.remainder and total_thread_needed > warehouse.remainder):
            return {'status': False, 'message': 'Not enough materials.'}

        return {'status': True}
