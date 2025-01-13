from django.urls import path
from rest_framework.routers import SimpleRouter
from habit.views import HabitViewSet, UserhabitListAPIView, HabitpublicityListAPIView
from habit.apps import HabitConfig

app_name = HabitConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [
    path("habitpublicity/", HabitpublicityListAPIView.as_view(), name="habitpublicity"),
    path("userhabit/", UserhabitListAPIView.as_view(), name="userhabit"),
]

urlpatterns += router.urls
