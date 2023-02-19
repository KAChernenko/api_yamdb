from rest_framework import viewsets

from .mixins import ModelMixinSet
from .serializers import GenreSerializer, CategorySerializer, TitleSerializer

from reviews.models import Genre, Category, Title

class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
