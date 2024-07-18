from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.reservations.models import Reservation
from apps.users.models import User


class Review(models.Model):
    renter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    rate = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rate must be between 1 and 5.'
    )
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='review')
