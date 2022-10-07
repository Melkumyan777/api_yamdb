from django.core.mail import send_mail
from reviews.models import User


def send_token(user: User):
    send_mail(
        'Добро пожаловать на проект YamDB!',
        (
            'Поздравляем! Вы только что зарегистрировались на нашем сервисе. '
            'Для подтверждения регистрации пожалуйста нашему API POST-запрос, '
            f'Содержащий код подтверждения: "{user.get_hash()}"\n'
            'Если Вы не регистрировались, проигнорируйте это письмо.\n\n'
            'С уважением, команда YamDB'
        ),
        'registration@yamdb.fake',
        [user.email],
        fail_silently=False,
    )
