from django.contrib import admin
from django.urls import path, include

import webpos_product.urls
import webpos_account.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include(webpos_product.urls, namespace='product')),
    path('api/account/', include(webpos_account.urls, namespace='account'))
]

