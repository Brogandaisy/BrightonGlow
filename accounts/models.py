from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                   message="Enter a valid phone number.")]
    )
    email = models.EmailField(unique=True, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_county = models.CharField(max_length=255, blank=True, null=True)
    address_country = models.CharField(max_length=255, blank=True, null=True)
    address_postcode = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    SKIN_TYPES = [
        ('Oily', 'Oily'),
        ('Dry', 'Dry'),
        ('Combination', 'Combination'),
        ('Sensitive', 'Sensitive'),
        ('Normal', 'Normal'),
    ]
    skin_type = models.CharField(
        max_length=20, choices=SKIN_TYPES, blank=True, null=True
        )

    def __str__(self):
        return (
            f"{self.full_name} ({self.user.username})"
            if self.full_name
            else self.user.username
        )
