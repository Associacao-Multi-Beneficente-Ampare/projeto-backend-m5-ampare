from rest_framework import permissions
import ipdb
from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsAdminOrUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return request.user == obj


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User) -> bool:
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_superuser
        )