from django.db import models
from django.core.validators import MaxLengthValidator

from apps.reservations.choices.lands import Lands


class Address(models.Model):
    land = models.CharField(max_length=25, choices=Lands.choices)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    postal_code = models.SmallIntegerField(validators=[MaxLengthValidator(5)])
