from django.conf import settings

subject = 'Добро пожаловать на проект YamDB!'
from_email = settings.YAMDB_WELCOME_EMAIL_FROM
message = (
    'Поздравляем! Вы только что зарегистрировались на нашем сервисе. '
    'Для подтверждения регистрации пожалуйста нашему API POST-запрос, '
    'Содержащий код подтверждения: "{code:s}"\n'
    'Если Вы не регистрировались, проигнорируйте это письмо.\n\n'
    'С уважением, команда YamDB'
)
