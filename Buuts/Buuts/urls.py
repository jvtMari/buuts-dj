from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),

    #ROUTERS
    path('api/accounts/', include('apps.accounts.routers')),
    path('api/shop/', include('apps.shop.routers'))
]
