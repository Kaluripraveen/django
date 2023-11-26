from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    profile_picture = forms.ImageField(
        required=False,  # Adjust based on your requirements
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )
    address_line1 = forms.CharField(
        max_length=255,
        required=False,  # Adjust based on your requirements
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    city = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    state = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    pincode = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode','is_patient','is_doctor')