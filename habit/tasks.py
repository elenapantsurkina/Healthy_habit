from celery import shared_task
from habit.services import send_telegram_message
from users.models import User
from habit.models import Habit


@shared_task
def send_information_telegram(tg_chat_id):
    """Отправляет пользователю напоминание о привычке."""
    message = f"Вам необходимо сделать {habit}."
    user = User.objects.get(tg_chat_id=tg_chat_id)
    if user.tg_chat_id:
        send_telegram_message(user.tg_chat_id, message)
