from rest_framework import permissions

class VendorPermission(permissions.BasePermission):
    """
    Custom permission to only allow vendors to access their own data.
    """

    def has_object_permission(self, request, view, obj):
        
        return obj == request.user.vendor


class AdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain API endpoints.
    """

    def has_permission(self, request, view):
        
        return request.user.is_superuser