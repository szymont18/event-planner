from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
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
        # TODO: ERROR WHEN USER WITH THIS ID ALREADY EXISTS


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control',
                                                            'type': 'text',
                                                            'placeholder': 'Enter Your email address'}),
                             validators=[validate_email])

    def clean_email(self):
        email = self.cleaned_data['email']

        # if not WebsiteUser.objects.filter(email=email).exists():
        #     print("!!!!!!!!!!!!!!!!!!!!!!")
        #     raise forms.ValidationError("This email address is not associated with any user account.")
        print(f'email = {email}')
        return email
