from django.conf import settings

subject = 'Добро пожаловать на проект YamDB!'
from_email = settings.YAMDB_WELCOME_EMAIL_FROM


def message(confirmation_code):
    message = (
        'Поздравляем! Вы только что зарегистрировались на нашем сервисе. '
        'Для подтверждения регистрации пожалуйста нашему API POST-запрос, '
        f'Содержащий код подтверждения: "{confirmation_code}"\n'
        'Если Вы не регистрировались, проигнорируйте это письмо.\n\n'
        'С уважением, команда YamDB'
    )
    return message
