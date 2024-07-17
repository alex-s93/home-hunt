from django.utils import timezone
from rest_framework import serializers

from apps.reviews.models import Review


class ApartmentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['renter', 'message', 'rate']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['renter']

    def validate(self, data):
        user = self.context['request'].user
        reservation = data.get('reservation')

        if reservation.renter != user:
            raise serializers.ValidationError(
                'You cannot review this reservation cause you are not an owner'
            )

        if reservation.date_to >= timezone.now().date():
            raise serializers.ValidationError(
                'This reservation is not completed'
            )

        if not reservation.is_approved_by_landlord:
            raise serializers.ValidationError(
                'You cannot review not approved reservation'
            )

        if reservation.is_canceled:
            raise serializers.ValidationError(
                'You cannot review canceled reservation'
            )

        return data
