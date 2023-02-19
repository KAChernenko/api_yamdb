from rest_framework import permissions


class IsRoleAdminOrSuperuser(permissions.BasePermission):
    """Доступ разрешен только для администратора и Супер юзера."""
    def has_permission(self, request, view):
        if request.user.role == 'admin' or request.user.is_superuser:
            return True
        return False


class IsRoleModerator(permissions.BasePermission):
    """Доступ разрешен только для Модератора."""
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'moderator':
            return True
        return False


class Title(permissions.BasePermission):
    """
    Предоставление прав доступа для администратора и супер юзера
    на добавление и удаление категорий, жанров и произведений.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.role == 'admin' or request.user.is_superuser:
            return True
        return False


class Review(permissions.BasePermission):
    """
    Предоставление прав доступа для авторов, администратора и модератора
    на изменение отзывов и комментариев.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
                or obj.author == request.user)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

