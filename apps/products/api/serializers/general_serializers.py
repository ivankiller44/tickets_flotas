from apps.products.models import Ubicacion, Descripcion, Fotos

from rest_framework import serializers

class UbicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ubicacion
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class DescripcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Descripcion
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class FotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fotos
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)