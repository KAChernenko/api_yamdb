from rest_framework import serializers
from reviews.models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    authot = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.SlugRelatedField(
        slug_field='name',
        default=serializers.CurrentUserDefault(),
        write_only=True
    )
    class Meta:
        model = Reviews
        fields = ('id', 'text', 'author', 'score', 'pub_date')
