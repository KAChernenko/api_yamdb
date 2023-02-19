from django.urls import path, include
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ReviewsViewSet

router = SimpleRouter()
router.register(r'titles/(?P<post_id>\d+)/reviews',ReviewsViewSet, 'reviews')
#http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

urlpatterns = [
    path('v1/', include(router.urls)),
]