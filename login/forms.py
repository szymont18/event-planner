from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import WebsiteUser


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = WebsiteUser
        fields = ['username', 'password']

        labels = {
            'username': "Your username",
            'password': "Your password"
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter Your username'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter Your password'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": 'form-control',
                                                     'type': 'text',
                                                     'placeholder': 'Enter Your username'})
        self.fields["password"].widget.attrs.update({'class': 'form-control',
                                                     'type': 'password',
                                                     'placeholder': 'Enter Your password'})
