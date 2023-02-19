from django.db import models

from .validators import validate_year


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
    

class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        validators=(validate_year, ),
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
