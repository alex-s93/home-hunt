from django.db import IntegrityError

from rest_framework import serializers

from apps.addresses.models import Address
from apps.addresses.serializers import AddressApartmentSerializer
from apps.apartments.models import Apartment


def get_or_create_address(address_data):
    address, created = Address.objects.get_or_create(
        land=address_data['land'],
        city=address_data['city'],
        street=address_data['street'],
        house_number=address_data['house_number'],
        postal_code=address_data['postal_code']
    )
    return address


class ApartmentSerializer(serializers.ModelSerializer):
    address = AddressApartmentSerializer()

    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = ['landlord']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = get_or_create_address(address_data)
        try:
            apartment = Apartment.objects.create(address=address, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return apartment

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address = get_or_create_address(address_data)
            instance.address = address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        try:
            instance.save()
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return instance


class ApartmentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
