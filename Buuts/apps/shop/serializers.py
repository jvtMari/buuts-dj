from rest_framework import serializers, pagination
#
from .models import *


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('__all__')


class DetailModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    
    class Meta:
        model = Model
        fields = (
            'name',
            'brand',
        )


class ModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Model
        fields = ('__all__')


class TaxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tax
        fields = ('__all__')


class SizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Size
        fields = ('__all__')


class DetailProductSerializer(serializers.ModelSerializer):
    model = DetailModelSerializer()
    tax = TaxSerializer()

    class Meta:
        model = Product
        fields = (
            'barcode',
            'model',
            'desc',
            'purchase_price',
            'sale_price',
            'tax',
            'out_stock',
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

    def validate(self, data):
        method = self.context.get('request').method
        if method == 'PATCH' and self.instance.barcode != data.get('barcode', None):
            raise serializers.ValidationError('Barcode can not be updated, PK product.')
        return super().validate(data)







class BasicPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 100
