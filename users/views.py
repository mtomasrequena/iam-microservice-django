from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint that allows any unauthenticated user to register.
    
    Method: POST
    Payload: email, password, first_name (optional), last_name (optional)
    Returns: 201 Created on success, 400 Bad Request on validation errors.
    """
    
    # Queryset is defined for DRF metadata and future Swagger/OpenAPI schema generation
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    
    # Override the global IsAuthenticated setting to allow public registration
    permission_classes = [AllowAny]