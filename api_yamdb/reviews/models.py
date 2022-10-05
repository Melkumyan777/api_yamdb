from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = (
    ('user', 'User'),
    ('moderator', 'Moderator'),
    ('admin', 'Admin')
)


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя пользователя'
    )
    role = models.CharField(
        choices=USER_ROLES,
        default='user',
        max_length=10,
        verbose_name='Роль на сайте'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='Является суперпользователем'
    )
    bio = models.TextField(
        verbose_name='Биография',
        null=True
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        max_length=254,
        verbose_name='Адрес электронной почты'
    )
