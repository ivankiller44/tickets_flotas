from apps.products.models import Departamento, Departamento1, TipoDeBus, NumeroDeBus, FechaDeSalida, HoraDeSalida

from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class Departamento1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento1
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

