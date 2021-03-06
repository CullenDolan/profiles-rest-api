from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
    
        return obj.id == request.user.id # will return true if user is trying to update their own profile


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update pwn status"""
    def has_object_permission(self, request, view, obj):
        """chcek the user is trying to update their own statys"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
        
