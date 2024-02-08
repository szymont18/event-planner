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
        fields = ['profile_picture', "username", "first_name", 'last_name', "email"]
        help_texts = {
            'username': None,
        }

