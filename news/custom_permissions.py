from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """"Permission for check user is owner or superuser"""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or bool(
            request.user and request.user.is_superuser
        )
