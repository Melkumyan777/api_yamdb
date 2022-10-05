from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = (
    ('user', 'User'),
    ('moder', 'Moderator'),
    ('admin', 'Admin')
)


class User(AbstractUser):
    role = models.CharField(choices=USER_ROLES, default='user', max_length=5)
    is_superuser = models.BooleanField(default=False)