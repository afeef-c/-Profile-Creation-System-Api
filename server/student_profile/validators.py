import re
from django.core.exceptions import ValidationError

def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must include at least one numeric digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must include at least one special character.")
