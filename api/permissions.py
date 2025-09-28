from rest_framework import permissions

class IsStaffOrOwner(permissions.BasePermission):
    """
    Custom permission to allow only staff users or the owner of an object to edit/delete
    """
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user and request.user.is_staff:
            return True
        
        return obj.user == request.user