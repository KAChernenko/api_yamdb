from django.db import models
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator)

MAX_SCORE = 10
MIN_SCORE = 1

class MyModel(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Время публикации'
    )
    class Meta:
        abstract = True

class Reviews(MyModel):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )

    author = models.IntegerField(
        #Заглушк, в последующем станет ссылкой на автора
    )

    title = models.IntegerField(
        #Заглушка, в последствии станет ссалкой на title
    )

    score = models.IntegerField(
        verbose_name='Оценка отзыва',
        validators=(
            MaxValueValidator(limit_value=MAX_SCORE),
            MinValueValidator(limit_value=MIN_SCORE),
        )
    )

    


class Comments(MyModel):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    author = models.IntegerField(
        #Заглушк, в последующем станет ссылкой на автора
    )
    review = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Review, которому пренадлежит комментарий'
    )
