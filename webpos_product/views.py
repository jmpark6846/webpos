from rest_framework.permissions import IsAuthenticated

from webpos_common.views import BaseViewSet
from webpos_product.models import Product
from webpos_product.serializers import ProductListSerializer, ProductCreateUpdateSerializer, ProductRetrieveSerializer


class ProductViewSet(BaseViewSet):
    permission_classes = (IsAuthenticated,)
    viewset_serializer_class = {
        'list': ProductListSerializer,
        'create': ProductCreateUpdateSerializer,
        'retrieve': ProductRetrieveSerializer,
        'update': ProductCreateUpdateSerializer
    }
    queryset = Product.objects.filter(deleted_at=None)


