from django.contrib import admin
from django.urls import include, path

# SimpleJWT views responsible for secure token generation and rotation
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Admin Panel Route
    path('admin/', admin.site.urls),
    
    # ==========================================
    # JWT Authentication Endpoints
    # ==========================================
    
    # POST /api/v1/auth/login/
    # Accepts valid user credentials (email and password).
    # Returns a short-lived access token and a long-lived refresh token.
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # POST /api/v1/auth/refresh/
    # Accepts a valid refresh token.
    # Returns a newly generated short-lived access token to maintain the session.
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ==========================================
    # Application Routing
    # ==========================================
    
    # Delegates all requests starting with '/api/v1/users/' to the 'users' app router
    path('api/v1/users/', include('users.urls', namespace='users')),
]