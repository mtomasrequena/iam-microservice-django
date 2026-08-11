from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
# Import our custom permissions and serializer
from .permissions import IsAdminRole, IsClientRole, IsKycVerified
from .serializers import KycStatusUpdateSerializer

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

class AdminUpdateKycView(generics.UpdateAPIView):
    """
    Endpoint for ADMIN users to update the KYC status of any user.
    Uses UpdateAPIView to handle PATCH/PUT requests automatically.
    """
    queryset = User.objects.all()
    serializer_class = KycStatusUpdateSerializer
    # DRF evaluates permissions in the list using logical AND.
    # The user MUST be authenticated (global setting) AND be an ADMIN.
    permission_classes = [IsAdminRole]
    
    # We use the default 'pk' in the URL to identify the user to update.
    # e.g., PATCH /api/v1/users/1/kyc/

class ClientProtectedDashboardView(APIView):
    """
    A sample endpoint representing a secure area exclusively for verified clients.
    (e.g., viewing financial assets or initiating a transaction).
    """
    # Here we stack permissions. The user must be a CLIENT *AND* have KYC verified.
    permission_classes = [IsClientRole, IsKycVerified]

    def get(self, request, *args, **kwargs):
        # If the code reaches this point, we are 100% sure the user is a verified client.
        # No need for extra if-statements inside the business logic.
        user_email = request.user.email
        
        return Response(
            {
                "message": "Welcome to the secure vault.",
                "user": user_email,
                "status": "KYC Verified - Full Access Granted"
            },
            status=status.HTTP_200_OK
        )