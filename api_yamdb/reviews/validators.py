import datetime

from django.core.exceptions import ValidationError


def year_validator(value):
    now = datetime.timezone.now().year
    if value > now:
        raise ValidationError(
            f'{value} не должно быть больше {now}'
        )