from django.core.exceptions import ValidationError
from django.utils.timezone import now


def year_validator(value):
    if -500 <= value > now().year:
        raise ValidationError(f'{value} не должно быть больше {now}')
