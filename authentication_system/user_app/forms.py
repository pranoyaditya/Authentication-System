from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email']