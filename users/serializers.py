from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Safely retrieve the CustomUser model configured in settings.py
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for handling new user registration.
    
    Responsibilities:
    - Validates incoming user data (email format, password strength).
    - Ensures passwords are write-only (never returned in HTTP responses).
    - Safely creates a new CustomUser instance applying password hashing.
    """
    
    # Enforce strict password validation and prevent it from being read/returned
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={'input_type': 'password'},
        help_text="Password must meet standard complexity requirements."
    )

    class Meta:
        model = User
        # Explicitly define the allowed fields to prevent Mass Assignment Vulnerabilities
        fields = ('email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        """
        Overrides the default create method to use our CustomUserManager.
        This guarantees the password is hashed via user.set_password() 
        instead of being saved as plain text.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class KycStatusUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer specifically designed for updating the KYC verification status.
    Exposes only the 'is_kyc_verified' field to prevent accidental updates 
    to other sensitive user data (Mass Assignment Vulnerability).
    """
    class Meta:
        model = User
        fields = ['is_kyc_verified']

class KycStatusSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for retrieving the KYC status of a user.
    Exposes the user's ID, email, and verification status for auditing purposes.
    Strictly prevents any write operations via read_only_fields.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'is_kyc_verified']
        # Defensive programming: ensure these fields cannot be modified via this serializer
        read_only_fields = ['id', 'email', 'is_kyc_verified']