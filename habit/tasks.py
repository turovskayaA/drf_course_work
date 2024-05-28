from datetime import datetime

from celery import shared_task

from habit.models import Habit
from habit.services import TelegramBot


@shared_task
def task_send_message():
    date_now = datetime.today().weekday()
    time_now = datetime.now().time().strftime("%H:%M")
    habits = Habit.objects.filter(is_pleasant=False)

    for habit in habits:
        if habit.time.strftime("%H:%M") == time_now and habit.period and date_now:
            chat_id = habit.user.tg_chat_id
            text_message = (
                f"Пора {habit.action} на {habit.place}. "
                f"Тебе необходимо примерно {habit.time_to_complete} секунд."
            )
            if habit.reward:
                text_message = f"\nИ получишь вознаграждение -  {habit.reward}."
            message = TelegramBot()
            message.send_habit(text=text_message, chat_id=chat_id)
