from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import (
    UserCreateApiView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDeleteAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="get"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
