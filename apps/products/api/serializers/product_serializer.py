from rest_framework import serializers

from apps.products.models import Viaje
from apps.products.api.serializers.general_serializers import OrigenSerializer, DestinoSerializer, TipoDeBusSerializer, NumeroDeBusSerializer, FechaDeSalidaSerializer, HoraDeSalidaSerializer

class ViajeSerializer(serializers.ModelSerializer):
    #measure_unit = serializers.StringRelatedField()
    #category_product = serializers.StringRelatedField()

    class Meta: 
        model = Viaje
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
 
            'id' : instance.id,
            #'origen' : instance.origen, 
            #'name' : instance.name,
            #'measure_unit' : instance.measure_unit.description,
            #'category_product' : instance.category_product.description,
        }