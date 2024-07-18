from django.urls import path

from apps.users.views import (
    LoginAPIView,
    LogoutUserAPIView,
    RegisterUserAPIView,
)

urlpatterns = [
    path('sign-up/', RegisterUserAPIView.as_view()),
    path('sign-in/', LoginAPIView.as_view()),
    path('logout/', LogoutUserAPIView.as_view()),
]
