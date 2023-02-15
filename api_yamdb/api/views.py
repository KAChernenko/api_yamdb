from rest_framework import viewsets
from .mixins import ModelMixinSet


class GenreViewSet(ModelMixinSet):
    pass


class CategoryViewSet(ModelMixinSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    pass