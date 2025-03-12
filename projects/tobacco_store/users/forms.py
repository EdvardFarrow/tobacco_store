from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
