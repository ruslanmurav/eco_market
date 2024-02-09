from rest_framework.generics import ListAPIView, RetrieveAPIView

from goods.models import Category, Product
from goods.serializers import CategorySerializer, ShortProductSerializer, FullProductSerializer


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ShortProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer
    lookup_field = 'id'

