from rest_framework.serializers import ModelSerializer

from webpos_product.models import Product


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

