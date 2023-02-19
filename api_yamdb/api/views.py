from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import ReviewsSerializer
from reviews.models import Titles, User
from django.shortcuts import get_object_or_404

class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        return title.reviews
    
    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        user = get_object_or_404(User, id=self.request.user)
        serializer.save(author=user, title=title)
