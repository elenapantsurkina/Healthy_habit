from rest_framework.viewsets import ModelViewSet
from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """Вьюсет для модели Привычка."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
