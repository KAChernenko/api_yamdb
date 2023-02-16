from django.urls import path, include

#http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

urlpatterns = [
    path('v1/titles/<int:title_id>/', include('reviews.urls'))
]