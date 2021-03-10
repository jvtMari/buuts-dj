from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
#
from .models import (
    Size,
    Tax,
    Brand,
    Model,
    Product,
    Item,
    Sale,
    SaleItem,
    SaleSend,
)
#
from .serializers import (
    BasicPagination,
    BrandSerializer,
    DetailModelSerializer,
    ModelSerializer,
    TaxSerializer,
    SizeSerializer,
    ProductSerializer,
    DetailProductSerializer,
)


class BrandViewSet (viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    #
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if (self.action in ['partial_update','create']):
            self.permission_classes.append(IsAdminUser)

        return [permission() for permission in self.permission_classes]


class ModelViewSet (viewsets.ModelViewSet):
    queryset = Model.objects.all()
    pagination_class = BasicPagination
    #
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if (self.action in ['partial_update','create','delete']):
            self.permission_classes.append(IsAdminUser)

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action in ['partial_update', 'create']:
            return ModelSerializer
        else:
            return DetailModelSerializer


class TaxViewSet (viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    #
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if (self.action in ['partial_update','create','delete']):
            self.permission_classes.append(IsAdminUser)

        return [permission() for permission in self.permission_classes]


class SizeViewSet (viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    #
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if (self.action in ['partial_update','create','delete']):
            self.permission_classes.append(IsAdminUser)

        return [permission() for permission in self.permission_classes]


class ProductViewSet (viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = BasicPagination
    #
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = []
    search_fields = ['^model__name', '^model__brand__name']
    #
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if (self.action in ['partial_update','create','delete']):
            self.permission_classes.append(IsAdminUser)

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action in ['partial_update', 'create']:
            return ProductSerializer
        else:
            return DetailProductSerializer
