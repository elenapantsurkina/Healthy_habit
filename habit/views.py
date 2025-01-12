from rest_framework.viewsets import ModelViewSet
from habit.models import Habit
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """Вьюсет для модели Привычка."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    """Метод для управления созданием объекта и автомат привязки создаваемого объекта к авторизованному пользователю."""
    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_permissions(self):
        """Метод определения действий в зависимости является ли пользователь владельцем."""
        if self.action in ["update", "retrieve"]:
            self.permission_classes = (IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()
