from datetime import timedelta

from rest_framework import serializers
from django.utils import timezone
from django.db.models import Q

from apps.apartments.models import Apartment
from apps.apartments.serializers import ApartmentSerializer
from apps.reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'


class AbstractReservationCreateDetailSerializer(serializers.ModelSerializer):
    def validate_apartment(self, value):
        if not Apartment.objects.filter(title=value, is_active=True).exists():
            raise serializers.ValidationError(
                'This apartment is disabled for reservations or does not exist'
            )
        return value

    def validate_date_from(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError(
                'Date From must be today or later'
            )
        return value

    def validate_date_to(self, value):
        if value < timezone.now().date() + timedelta(days=1):
            raise serializers.ValidationError(
                'Date To must be tomorrow or later'
            )
        return value


class ReservationDetailsSerializer(AbstractReservationCreateDetailSerializer):
    class Meta:
        model = Reservation
        fields = [
            'apartment',
            'date_from',
            'date_to',
            'is_approved_by_landlord',
            'is_canceled',
        ]
        read_only_fields = [
            'is_approved_by_landlord',
            'is_canceled',
        ]

    def validate(self, data):
        date_from = data.get('date_from')
        date_to = data.get('date_to')
        apartment = data.get('apartment')

        if date_from or date_to:
            if apartment is None:
                apartment = self.instance.apartment
            if date_from is None:
                date_from = self.instance.date_from
            if date_to is None:
                date_to = self.instance.date_to

            if date_from >= date_to:
                raise serializers.ValidationError(
                    'Date From must be less than Date To'
                )

            check_dates_availability(apartment, date_from, date_to, self.instance.id)

        return data


class ReservationCreateSerializer(AbstractReservationCreateDetailSerializer):
    class Meta:
        model = Reservation
        fields = ('renter', 'apartment', 'date_from', 'date_to')
        read_only_fields = ['renter']

    def validate(self, data):
        date_from = data.get('date_from')
        date_to = data.get('date_to')
        apartment = data.get('apartment')

        if date_from >= date_to:
            raise serializers.ValidationError(
                'Date From must be less than Date To'
            )

        check_dates_availability(apartment, date_from, date_to)

        return data


class CancelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = [
            'renter',
            'apartment',
            'date_from',
            'date_to',
            'is_approved_by_landlord',
        ]


class ApproveReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = [
            'renter',
            'apartment',
            'date_from',
            'date_to',
            'is_canceled',
        ]


def check_dates_availability(apartment, date_from, date_to, reservation_id=None):
    overlapping_reservations = (Reservation.objects.filter(
        apartment=apartment,
        is_canceled=False,
        is_approved_by_landlord=True
    ).exclude(id=reservation_id).filter(
        Q(date_from__lte=date_to) & Q(date_to__gte=date_from)
    ))

    if overlapping_reservations.exists():
        raise serializers.ValidationError(
            'The apartment is already reserved for the selected dates. '
        )
