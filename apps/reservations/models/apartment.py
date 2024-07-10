from django.db import models
from django.db.models import Avg

from apps.reservations.choices.apartment_types import ApartmentTypes
from apps.users.models import User


class Apartment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    landlord = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='apartments'
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.SET_NULL,
        related_name='apartments',
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rooms = models.SmallIntegerField()
    apartment_type = models.CharField(max_length=20, choices=ApartmentTypes.choices, default=ApartmentTypes.APARTMENT)
    is_active = models.BooleanField(default=True)

    @property
    def avg_rate(self):
        return self.reviews.aggregate(avg_rate=Avg('rate'))['avg_rate'] or 0

    def __str__(self):
        return self.title
