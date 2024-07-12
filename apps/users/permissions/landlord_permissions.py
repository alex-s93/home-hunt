from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerLandlord(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.landlord == request.user or request.user.is_staff


class IsLandlordOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and (request.user.is_landlord or request.user.is_staff)
        )
