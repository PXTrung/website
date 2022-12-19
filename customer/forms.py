from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    phone = forms.CharField(
        required=True,
        max_length=11,
        widget=forms.TextInput(attrs={"class": "form-control mt-1 mb-3"}),
    )

    address = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mt-1 mb-3"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        help_texts = {
            'username': (''),
        }

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mt-1 mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mt-1 mb-3"}),
            "password": forms.PasswordInput(attrs={"class": "form-control mt-1 mb-3"}),
        }
