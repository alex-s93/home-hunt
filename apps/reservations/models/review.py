from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    rate = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rate must be between 1 and 5.'
    )
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, related_name='reviews')
