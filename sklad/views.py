# Assalawma aleykum mende tek bir dictionary bolip shiqti har bir partiya ushin bolek shigatugin etip isley almadim
from django.db.models import Sum
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from sklad.models import Warehouse, Material, Product, ProductMaterial


class ProductView(APIView):

    def post(self, request):
        product_code = request.data.get("code")
        quantity = request.data.get("qty")

        if not product_code or not quantity:
            return Response({"error": "Code and quantity are required."}, status=status.HTTP_400_BAD_REQUEST)

        materials_check = self.check_materials_for_shirts(quantity)
        if materials_check['status'] is False:
            return Response(materials_check['message'], status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "product_name": 'Koylak',
            "product_qty": quantity,
            "required_materials": materials_check['materials']
        }, status=status.HTTP_201_CREATED)

    def shirt(self):
        koylek_mato = 0.8
        koylek_tugma = 5
        koylek_ip = 10

        return {
            'koylek_mato': koylek_mato,
            'koylek_tugma': koylek_tugma,
            'koylek_ip': koylek_ip
        }

    def check_materials_for_shirts(self, quantity):
        shirt = self.shirt()
        jami_koylek_mato = quantity * shirt['koylek_mato']
        jami_koylek_tugma = quantity * shirt['koylek_tugma']
        jami_koylek_ip = quantity * shirt['koylek_ip']

        material_mato = Material.objects.filter(name='Mato').first()
        material_tugma = Material.objects.filter(name='Tugma').first()
        material_ip = Material.objects.filter(name='Ip').first()

        if not material_mato or not material_tugma or not material_ip:
            return {'status': False, 'message': "Material does not exist."}

        remainder_mato = \
        Warehouse.objects.filter(material_id=material_mato).aggregate(total_remainder=Sum('remainder'))[
            'total_remainder']
        remainder_tugma = \
        Warehouse.objects.filter(material_id=material_tugma).aggregate(total_remainder=Sum('remainder'))[
            'total_remainder']
        remainder_ip = Warehouse.objects.filter(material_id=material_ip).aggregate(total_remainder=Sum('remainder'))[
            'total_remainder']

        if (remainder_mato is None or remainder_mato < jami_koylek_mato) or \
                (remainder_tugma is None or remainder_tugma < jami_koylek_tugma) or \
                (remainder_ip is None or remainder_ip < jami_koylek_ip):
            return {'status': False, 'message': "Not enough materials available."}

        materials = {
            'Mato': jami_koylek_mato,
            'Tugma': jami_koylek_tugma,
            'Ip': jami_koylek_ip
        }

        return {'status': True, 'materials': materials}
