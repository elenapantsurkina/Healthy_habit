from rest_framework.serializers import ValidationError
from datetime import timedelta


def validator_time(value):
    """Проверяет продолжительность выполнения привычки не более 120 секунд."""
    if value:
        if value > timedelta(seconds=120):
            raise ValidationError("Продолжительность выполнения привычки не может быть более 120 секунд")


class WeeklyHabitValidator:
    """Проверяет периодичность выполнения привычки раз в 7 дней."""
    def __call__(self, value):
        if value.periodicity is not None and value.periodicity > 7:
            raise ValidationError("Периодичность выполнения привычки не может превышать 7 дней.")

        if value.periodicity is not None and value.periodicity < 1:
            raise ValidationError("Привычка должна выполняться хотя бы один раз в неделю.")


class HabitValidator:
    """Проверяет, что не заполнены одновременно поля "связанная привычка" и "вознаграждение"."""
    def __call__(self, value):
        related_habit = value.related_habit
        award = value.award
        if related_habit and award:
            raise ValidationError("Вы можете заполнить только одно из полей:'связанная привычка' или 'вознаграждение'.")


class PleasantHabitValidator:
    """Проверяет, что связанные привычки могут быть только с признаком "приятной привычки"."""
    def __call__(self, value):
        if value.related_habit is not None:
            related_habit = value.related_habit
            if not related_habit.pleasant_habit:
                raise ValidationError("Связанная привычка должна быть с признаком 'приятной привычки'.")


class RelatedHabitValidator:
    """Проверяет, что у приятной привычки не может быть вознаграждения или связанной привычки."""
    def __call__(self, value):
        if value.pleasant_habit:
            if value.award or value.related_habit:
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
