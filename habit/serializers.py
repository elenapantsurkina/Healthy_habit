from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from habit.models import Habit
from habit.validators import (WeeklyHabitValidator,
                              validator_time, HabitValidator, PleasantHabitValidator, RelatedHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    validators = [
        validator_time,
        WeeklyHabitValidator(),
        HabitValidator(),
        PleasantHabitValidator(),
        RelatedHabitValidator(),

    ]

    class Meta:
        model = Habit
        fields = "__all__"


class HabitpublicitySerializer(ModelSerializer):
    habitpublicity = SerializerMethodField()

    def get_habitpublicity(self, obj):
        # Получаем текущего пользователя из контекста
        user = self.context['request'].user
        # Фильтруем привычки по пользователю и статусу публикации
        return [habit.habit for habit in Habit.objects.filter(owner=user, publicity="Опубликована")]


class UserHabitSerializer(ModelSerializer):
    habituser = SerializerMethodField()

    def get_habituser(self, obj):
        # Получаем текущего пользователя из контекста
        user = self.context["request"].user
        return [habit.habit for habit in Habit.objects.filter(owner=user)]

    class Meta:
        model = Habit
        fields = "__all__"
