from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"

class SignUpRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        error_class = "error"
