from rest_framework.exceptions import ValidationError


class ExceptionHabitValidator:
    """Валидатор, для исключения одновременного выбора
    связанной привычки и указания вознаграждения."""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError("Необходимо добавить что-то одно!")


class DateHabitValidator:
    """Валидатор, для ограничения времени."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if "time_to_complete" in dict(value):
            time_to_complete = dict(value).get(self.field)

            if time_to_complete and time_to_complete >= 120:
                raise ValidationError(
                    "Превышено время выполнения привычки, не более 120 секунд!"
                )


class RelatedHabitValidator:
    """Валидатор для проверки, что связанная привычка является приятной."""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        if value:
            related_habit = dict(value).get(self.field1)
            if related_habit and not related_habit.is_pleasant:
                raise ValidationError(
                    "Связанной привычкой может быть только приятная привычка!"
                )


class NiceHabitValidator:
    """
    Валидатор для проверки, что у приятной привычки нет связанной привычки и вознаграждения.
    """

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_pleasant = dict(value).get(self.field3)

        if is_pleasant:
            if related_habit:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки!"
                )
            if reward:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения!"
                )


class PeriodHabitValidator:
    """
    Валидатор для проверки, что периодичность выполнения привычки находится в диапазоне от 1 до 7 дней.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if "period" in dict(value):
            period = dict(value).get(self.field)

            if period and (period < 1 or period > 7):
                raise ValidationError(
                    "Интервал задания периодичности должен быть от 1 до 7 дней!"
                )
            if period == 0:
                raise ValidationError("Периодичность не может быть равна нулю!")
