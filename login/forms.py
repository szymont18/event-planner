from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django import forms
from .models import WebsiteUser
from django.core.validators import validate_email


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


class RegisterForm(UserCreationForm):
    class Meta:
        model = WebsiteUser
        fields = ["username", "first_name", 'last_name', "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": 'form-control',
                                                     'type': 'text',
                                                     'placeholder': 'Enter Your username'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control',
                                                      'type': 'password',
                                                      'placeholder': 'Enter Your password'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control',
                                                      'type': 'password',
                                                      'placeholder': 'Confirm your password'})
        self.fields["email"].widget.attrs.update({"class": 'form-control',
                                                  'type': 'text',
                                                  'placeholder': 'Enter Your email address'})
        self.fields["first_name"].widget.attrs.update({"class": 'form-control',
                                                       'type': 'text',
                                                       'placeholder': 'Enter Your first name'})
        self.fields["last_name"].widget.attrs.update({"class": 'form-control',
                                                      'type': 'text',
                                                      'placeholder': 'Enter Your last name'})

    def is_valid(self):
        return super().is_valid()


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control',
                                                            'type': 'text',
                                                            'placeholder': 'Enter Your email address'}),
                             validators=[validate_email])

    def clean_email(self):
        email = self.cleaned_data['email']

        return email


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = WebsiteUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control',
                                                          'type': 'password',
                                                          'placeholder': 'Enter new password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control',
                                                          'type': 'password',
                                                          'placeholder': 'Repeat new password'})
