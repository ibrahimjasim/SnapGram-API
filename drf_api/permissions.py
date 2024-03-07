from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsNotificationOwner(permissions.BasePermission):
    """A custom permission class that restricts access to notifications, 
    ensuring that only the owner of the notification can view or modify it."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        raise PermissionDenied(
            "403 Permission denied"
        )