from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import signup, jwt_token, username_email


router_v1 = DefaultRouter()
# router_v1.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', jwt_token, name='jwt_token'),
    path('v1/auth/code/', username_email, name='username_email'),
    path('', include(router_v1.urls)),
]
