from django.urls import path
from .views import (
    AuditorKycStatusView,
    UserRegistrationView, 
    AdminUpdateKycView, 
    ClientProtectedDashboardView
)

# App namespace to avoid URL name collisions across different applications.
# Example usage in code: reverse('users:user-register')
app_name = 'users'

urlpatterns = [
    # POST /api/v1/users/register/
    # Public endpoint for new user registration.
    path('register/', UserRegistrationView.as_view(), name='user-register'),

    # PATCH /api/v1/users/<pk>/kyc/
    # Endpoint for administrators to update a user's KYC status.
    path('<int:pk>/kyc/', AdminUpdateKycView.as_view(), name='admin-update-kyc'),

    # GET /api/v1/users/client-dashboard/
    # Protected endpoint for verified clients to access their dashboard.
    path('client-dashboard/', ClientProtectedDashboardView.as_view(), name='client-dashboard'),
    
    # GET /api/v1/users/auditor/<pk>/kyc/
    # Endpoint for auditors to retrieve a user's KYC status.
    path('auditor/<int:pk>/kyc/', AuditorKycStatusView.as_view(), name='auditor-kyc-status'),
]