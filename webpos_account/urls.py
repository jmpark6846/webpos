from django.urls import path
from rest_framework.routers import SimpleRouter
from webpos_account.apps import WebposAccountConfig
from webpos_account.views import AccountViewSet, TokenView, AccountView

app_name = WebposAccountConfig.name

routers = SimpleRouter()
routers.register('', AccountViewSet, base_name='account')
urlpatterns = [
    path('create/', AccountView.as_view(), name='account-create'),
    path('token/', TokenView.as_view(), name='token')
]

urlpatterns += routers.urls
