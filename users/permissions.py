from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff == True


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
