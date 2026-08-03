from django.contrib import admin
from django.urls import path
# Import SimpleJWT views responsible for secure token generation and rotation.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Authentication Endpoints
    
    # POST /api/v1/auth/login/
    # Receives valid user credentials (email and password).
    # Returns a short-lived access token and a long-lived refresh token.
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # POST /api/v1/auth/refresh/
    # Receives a valid refresh token.
    # Returns a newly generated short-lived access token to keep the session alive securely.
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]