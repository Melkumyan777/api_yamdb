from django.core.exceptions import ValidationError
from django.utils.timezone import now


def year_validator(value):
    if value > now().year:
        raise ValidationError(f'{value} не должно быть больше {now}')
