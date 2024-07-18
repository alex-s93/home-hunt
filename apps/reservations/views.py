from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import SAFE_METHODS

from apps.reservations.models import Reservation
from apps.reservations.serializers import (
    ReservationCreateSerializer,
    ReservationSerializer,
    ReservationDetailsSerializer,
    CancelReservationSerializer,
    ApproveReservationSerializer
)
from apps.users.permissions.landlord_permissions import (
    IsLandlordOwnerOfReservationApartment,
    IsLandlord
)
from apps.users.permissions.renter_permissions import (
    IsRenterOwner,
    IsRenter
)


class ReservationListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReservationCreateSerializer
        else:
            return ReservationSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_landlord:
            return Reservation.objects.filter(apartment__landlord=user)
        else:
            return Reservation.objects.filter(renter=user)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsRenter | IsLandlord]
        else:
            self.permission_classes = [IsRenter]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


class ReservationDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationDetailsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [
                IsRenterOwner |
                IsLandlordOwnerOfReservationApartment
            ]
        else:
            self.permission_classes = [
                IsRenterOwner
            ]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Reservation.objects.none()

        if user.is_landlord:
            return Reservation.objects.filter(apartment__landlord=user)
        else:
            return Reservation.objects.filter(renter=user)

    def get_object(self):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class ReservationCancelView(UpdateAPIView):
    permission_classes = [IsRenterOwner]
    serializer_class = CancelReservationSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Reservation.objects.none()

        return Reservation.objects.filter(renter=user)

    def get_object(self):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class ReservationApproveView(UpdateAPIView):
    permission_classes = [IsLandlordOwnerOfReservationApartment]
    serializer_class = ApproveReservationSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Reservation.objects.none()

        return Reservation.objects.filter(apartment__landlord=user, is_canceled=False)

    def get_object(self):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
