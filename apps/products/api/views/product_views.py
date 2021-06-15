from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ViajeSerializer

class ViajeListAPIView(GeneralListAPIView):
    serializer_class = ViajeSerializer
    