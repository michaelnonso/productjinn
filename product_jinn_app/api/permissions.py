from rest_framework import permissions

#if user is admin he can edit but other users are read only

class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view): 
        if request.method in permissions.SAFE_METHODS: #check if doing GET which is safe
            return True
        else:   #if they are doin PUT,POST or DESTROY
            return bool(request.user and request.user.is_staff) #if user is loggedin and if he is admin
    
    
class IsUserReviewerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #check if doing GET which is safe
            return True
        else:   #if they are doin PUT,POST or DESTROY
            return obj.owner == request.user or request.user.is_staff
       
    