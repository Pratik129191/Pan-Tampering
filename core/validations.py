from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User


def is_email_validated(email):
    try:
        validate_email(email)
    except ValidationError:
        return False
    return True


def get_username_of_this(email):
    user = User.objects.get(email=email)
    return user.username


