from django.forms import ModelForm
from login.models import WebsiteUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class ProfileForm(ModelForm):
    class Meta:
        model = WebsiteUser
        fields = ["username", "first_name", 'last_name', "email"]
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({"class": 'form-control',
                                                                'type': 'text',
                                                                'placeholder': 'Enter Your Username'})
        self.fields['first_name'].widget.attrs.update({"class": 'form-control',
                                                     'type': 'text',
                                                     'placeholder': 'Enter Your First Name'})
        self.fields['last_name'].widget.attrs.update({"class": 'form-control',
                                                     'type': 'text',
                                                     'placeholder': 'Enter Your Last Name'})
        self.fields['email'].widget.attrs.update({"class": 'form-control',
                                                     'type': 'text',
                                                     'placeholder': 'Enter Your Email'})



