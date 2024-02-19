from django.contrib.auth import get_user_model
from django.contrib.auth import forms


class SignUpForm(forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "last_name", "first_name"]
