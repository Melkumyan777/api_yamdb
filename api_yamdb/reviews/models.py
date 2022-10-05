from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='reviews'
    )
    score = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ordering = ('pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments'
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ordering = ('pub_date',)
