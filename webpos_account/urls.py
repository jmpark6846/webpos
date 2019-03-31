from django.urls import path
from rest_framework.routers import SimpleRouter
from webpos_account.apps import WebposAccountConfig
from webpos_account.views import AccountViewSet, TokenView

app_name = WebposAccountConfig.name

routers = SimpleRouter()
routers.register('', AccountViewSet, base_name='account')

urlpatterns = [
    path('token/', TokenView.as_view(),)
]

urlpatterns += routers.urls
