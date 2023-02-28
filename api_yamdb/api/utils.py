from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404

from reviews.models import User


def generate_and_send_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код подтвержения для регистрации',
        f'Ваш код для получения токена {confirmation_code}',
        settings.EMAIL_ADMIN,
        [user.email],
        fail_silently=False,
    )
    user.save()
