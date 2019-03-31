from rest_framework.routers import SimpleRouter
from webpos_product.apps import WebposProductConfig
from webpos_product.views import ProductViewSet

app_name = WebposProductConfig.name

routers = SimpleRouter()
routers.register('', ProductViewSet, base_name='product')

urlpatterns = []

urlpatterns += routers.urls
