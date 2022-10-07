# import datetime
from django.utils.timezone import now

from django.core.exceptions import ValidationError


def year_validator(value):
    if value > now().year:
        raise ValidationError(
            f'{value} не должно быть больше {now}'
        )

# def year_validator(value):
#     now = datetime.timezone.now().year
#     if value > now:
#         raise ValidationError(
#             f'{value} не должно быть больше {now}'
#         )