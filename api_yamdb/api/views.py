from rest_framework import viewsets
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .filters import TitleFilter
from .mixins import ModelMixinSet
from .permissions import IsRoleAdminOrSuperuser, Title
from .serializers import (SignupSerializer, TokenSerializer, UserSerializer,
                          GenreSerializer, CategorySerializer, TitleSerializer,
                          TitleCreateSerializer, AdminUserSerializer
                          )
from api_yamdb.settings import ADMIN_EMAIL
from reviews.models import User, Genre, Category, Title


class UserViewSet(viewsets.ModelViewSet):
    """
    Доступ только у администратора
    """
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (IsRoleAdminOrSuperuser,)
    filter_backends = (SearchFilter,)
    lookup_field = 'username'
    lookup_value_regex = r'[\w\@\.\+\-]+'
    search_fields = ('username',)

    @action(
        detail=False, methods=['get', 'patch'],
        url_path='me', url_name='me',
        permission_classes=(IsAuthenticated,)
    )
    def about_me(self, request):
        serializer = UserSerializer(request.user)
        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsRoleAdminOrSuperuser,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    lookup_field = 'slug'


class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsRoleAdminOrSuperuser,)
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination
    filter_class = filterset_class = TitleFilter
    permission_classes = (IsRoleAdminOrSuperuser,)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH',):
            return TitleCreateSerializer
        return TitleSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """
    Создание пользователя, отправка кода на эл.почту
    """
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_confirmation_code(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.data['username']
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.data['confirmation_code']
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    token = RefreshToken.for_user(user)
    return Response(
        {'token': str(token.access_token)}, status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def username_email(request):
    """
    Если код утерян, отправить имя пользователя и эл.почту
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        email = serializer.data['email']
        user = get_object_or_404(User, username=username, email=email)
        send_confirmation_code(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_confirmation_code(user):
    """
    Отправка кода по почте
    """
    confirmation_code = default_token_generator.make_token(user)
    subject = 'Код подтверждения YaMDb'
    message = f'{confirmation_code} - ваш код для авторизации на YaMDb'
    admin_email = ADMIN_EMAIL
    user_email = [user.email]
    return send_mail(subject, message, admin_email, user_email)
