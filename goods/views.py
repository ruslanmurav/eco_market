from rest_framework.generics import ListAPIView

from goods.models import Category
from goods.serializers import CategorySerializer


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


