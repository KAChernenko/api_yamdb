from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
                signup, jwt_token, username_email,
                CategoryViewSet, GenreViewSet, TitleViewSet,
                ReviewsViewSet, CommentsViewSet, UserViewSet
            )


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)' r'/comments',
    CommentsViewSet,
    basename='comments',
)
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', jwt_token, name='jwt_token'),
    path('v1/auth/code/', username_email, name='username_email'),
    path('v1/', include(router_v1.urls)),
]
