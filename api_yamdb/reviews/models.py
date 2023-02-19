from django.db import models
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator)
from django.contrib.auth.models import AbstractUser
MAX_SCORE = 10
MIN_SCORE = 1
ROLE = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class MyModel(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Время публикации'
    )
    class Meta:
        abstract = True


class User(AbstractUser):
    """Модель для работы с пользователями"""
    username = models.CharField(
        max_length=200,
        unique=True
    )
    email = models.EmailField(
        unique=True,
        max_length=255,
        verbose_name='Адрес электронной почты'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='Биография'
    )
    role = models.CharField(
        max_length=15,
        choices=ROLE,
        default='user',
        verbose_name='Роль'
    )
    password = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

class Category(models.Model):
    """Категории произведений."""
    name = models.CharField(
        max_length=256,
        verbose_name='Имя категории'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Слаг категории'
    )


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    """Категории произведений."""
    name = models.CharField(
        max_length=256,
        verbose_name='Имя жанра'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Слаг жанра'
    )


    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        verbose_name='Год'
        )
    description = models.TextField(
        max_length=256,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )


    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self) -> str:
        return self.name



class Reviews(MyModel):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    score = models.IntegerField(
        verbose_name='Оценка отзыва',
        validators=(
            MaxValueValidator(limit_value=MAX_SCORE),
            MinValueValidator(limit_value=MIN_SCORE),
        )
    )

    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self) -> str:
        return self.text

    
class Comments(MyModel):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    author = models.models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Review, которому пренадлежит комментарий'
    )

    def __str__(self) -> str:
        return self.text
