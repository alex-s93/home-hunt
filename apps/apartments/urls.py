from django.urls import path

from apps.apartments.views import (
    ApartmentListCreateView,
    ApartmentDetailUpdateDeleteView
)

urlpatterns = [
    path("", ApartmentListCreateView.as_view()),
    path("<int:pk>/", ApartmentDetailUpdateDeleteView.as_view()),
]
