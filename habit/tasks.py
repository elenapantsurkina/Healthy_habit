from celery import shared_task
from habit.services import send_telegram_message
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from habit.models import Habit
from datetime import datetime, timedelta
import pytz
from config import settings


@shared_task
def send_information_telegram(tg_chat_id):
    """Отправляет пользователю напоминание о привычке."""
    time_zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.now(time_zone)

    # Фильтруем привычки в диапазоне следующего часа
    start_time = current_time.time()
    end_time = (datetime.now(time_zone) + timedelta(hours=1)).time()
    habits = Habit.objects.filter(time_habit__range=(start_time, end_time))

    if not habits.exists():
        return

    try:
        user = User.objects.get(tg_chat_id=tg_chat_id)
    except ObjectDoesNotExist:
        return f"Пользователь с данным {tg_chat_id} не найден"

    for habit in habits:
        message = f"Вам необходимо сделать {habit.action} в {habit.time_habit} в {habit.location}."
        send_telegram_message(user.tg_chat_id, message)
