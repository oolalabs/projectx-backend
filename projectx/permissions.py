from rest_framework import permissions
from rest_framework.compat import is_authenticated
from django.conf import settings

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
UNSAFE_METHODS = ('PUT', 'POST', 'PATCH')

class AllowAnyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class AuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return is_authenticated(request.user)


class SuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in SAFE_METHODS


class MainUserViewSetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (request.method in list(SAFE_METHODS)+["POST"] and view.action != "list")

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return True
        return obj.pk == request.user.pk