from django.contrib import admin
from .models import *

admin.site.register(Size)
admin.site.register(Tax)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(SaleSend)

