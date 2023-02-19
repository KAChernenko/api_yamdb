from django.db import models
from django.contrib.auth.models import AbstractUser


ROLE = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


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
