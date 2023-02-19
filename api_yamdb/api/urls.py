from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import signup, jwt_token, username_email, CategoryViewSet, GenreViewSet, TitleViewSet


router_v1 = DefaultRouter()
# router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)

urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', jwt_token, name='jwt_token'),
    path('v1/auth/code/', username_email, name='username_email'),
    path('', include(router_v1.urls)),
]
