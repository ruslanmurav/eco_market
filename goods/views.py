from rest_framework.generics import ListAPIView, RetrieveAPIView

from goods.models import Category, Product
from goods.serializers import CategorySerializer, ShortProductSerializer, FullProductSerializer


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ShortProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer
    lookup_field = 'id'

