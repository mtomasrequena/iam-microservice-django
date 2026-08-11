from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """
    Custom permission class to grant access exclusively to users with the 'ADMIN' role.
    Used for endpoints that require administrative privileges (e.g., user management, global settings).
    """
    def has_permission(self, request, view):
        # Defensive programming: always check if the user is authenticated first, 
        # even if IsAuthenticated is set globally. This prevents AnonymousUser errors 
        # if a specific view overrides the global permissions.
        return bool(request.user and request.user.is_authenticated and request.user.role == 'ADMIN')


class IsClientRole(BasePermission):
    """
    Custom permission class to grant access exclusively to users with the 'CLIENT' role.
    Used for standard end-user operations.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'CLIENT')


class IsAuditorRole(BasePermission):
    """
    Custom permission class to grant access exclusively to users with the 'AUDITOR' role.
    Typically used for read-only endpoints required for compliance or monitoring.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'AUDITOR')


class IsKycVerified(BasePermission):
    """
    Custom permission class to verify if the authenticated user has completed the KYC 
    (Know Your Customer) verification process. 
    Can be chained logically with role permissions in the views using bitwise operators.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_kyc_verified)