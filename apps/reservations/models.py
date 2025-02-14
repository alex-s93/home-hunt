from django.db import models

from apps.apartments.models import Apartment
from apps.users.models import User


class Reservation(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='reservations')
    date_from = models.DateField()
    date_to = models.DateField()
    is_approved_by_landlord = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

