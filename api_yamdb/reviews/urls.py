from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

ururlpatterns = [
    path('',include(router.urls))
]