from django.urls import path

from apps.reviews.views import (
    ReviewListCreateView,
    ReviewDetailUpdateDeleteView
)

urlpatterns = [
    path("", ReviewListCreateView.as_view()),
    path("<int:pk>/", ReviewDetailUpdateDeleteView.as_view()),
]
