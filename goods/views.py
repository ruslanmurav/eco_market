from rest_framework.generics import ListAPIView

from goods.models import Category, Product
from goods.serializers import CategorySerializer, ShortProductSerializer


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ShortProductSerializer




