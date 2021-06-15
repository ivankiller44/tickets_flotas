from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import OrigenSerializer, DestinoSerializer, TipoDeBusSerializer, NumeroDeBusSerializer, FechaDeSalidaSerializer, HoraDeSalidaSerializer

class OrigenListAPIView(GeneralListAPIView):
    serializer_class = OrigenSerializer

class DestinoListAPIView(GeneralListAPIView):
    serializer_class = DestinoSerializer

class TipoDeBusListAPIView(GeneralListAPIView):
    serializer_class = TipoDeBusSerializer

class NumeroDeBusListAPIView(GeneralListAPIView):
    serializer_class = NumeroDeBusSerializer

class FechaDeSalidaListAPIView(GeneralListAPIView):
    serializer_class = FechaDeSalidaSerializer

class HoraDeSalidaListAPIView(GeneralListAPIView):
    serializer_class = HoraDeSalidaSerializer
