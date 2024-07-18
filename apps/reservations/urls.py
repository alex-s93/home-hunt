from django.urls import path

from apps.reservations.views import (
    ReservationListCreateView,
    ReservationDetailUpdateDeleteView,
    ReservationCancelView,
    ReservationApproveView
)

urlpatterns = [
    path("", ReservationListCreateView.as_view()),
    path("<int:pk>/", ReservationDetailUpdateDeleteView.as_view()),
    path("<int:pk>/approve/", ReservationApproveView.as_view()),
    path("<int:pk>/cancel/", ReservationCancelView.as_view()),
]
