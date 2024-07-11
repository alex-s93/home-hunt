from rest_framework.permissions import BasePermission


class IsOwnerRenter(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = obj.renter or obj.apartment.landlord
        return request.user == user
