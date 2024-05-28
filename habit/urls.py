from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitCreateApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
    UserHabitListApiView,
)

app_name = HabitConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateApiView.as_view(), name="create"),
    path("habit/", HabitListApiView.as_view(), name="list"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="get"),
    path("habit/update/<int:pk>/", HabitUpdateApiView.as_view(), name="update"),
    path("habit/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete"),
    path("habit/public_list/", UserHabitListApiView.as_view(), name="public_list"),
]
