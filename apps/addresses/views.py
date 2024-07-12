from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.addresses.models import Address
from apps.addresses.serializers import AddressSerializer
from apps.users.permissions.landlord_permissions import IsLandlordOrAdmin


class AddressListCreateView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = [IsLandlordOrAdmin]


class AddressDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = [IsLandlordOrAdmin]
