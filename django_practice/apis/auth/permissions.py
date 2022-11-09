from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        return request.user.is_authenticated and request.user.is_active


class IsAuthenticatedOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and super().has_permission(request=request, view=view)


class JohnyWhiskyIsAdminUser(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_staff and super().has_permission(request=request, view=view)


class JohnyWhiskyIsSuperAdminUser(JohnyWhiskyIsAdminUser):
    ...
