from django.urls import path
from .views import UserRegistrationView

# App namespace to avoid URL name collisions across different applications.
# Example usage in code: reverse('users:user-register')
app_name = 'users'

urlpatterns = [
    # POST /api/v1/users/register/
    # Public endpoint for new user registration.
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]