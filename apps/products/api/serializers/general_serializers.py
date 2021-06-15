from apps.products.models import Origen, Destino, TipoDeBus, NumeroDeBus, FechaDeSalida, HoraDeSalida

from rest_framework import serializers

class OrigenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origen
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class TipoDeBusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDeBus
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class NumeroDeBusSerializer(serializers.ModelSerializer):

    class Meta:
        model = NumeroDeBus
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)
        
class FechaDeSalidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FechaDeSalida
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class HoraDeSalidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = HoraDeSalida
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

