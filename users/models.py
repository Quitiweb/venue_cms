from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    phone = PhoneNumberField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_avno = models.BooleanField(
        "avno user",
        default=False,
        help_text="Designates whether this user should be treated as an AVNO user."
    )


class UserAdmin(Account):
    avno_user = models.CharField(default='', max_length=150)

    class Meta:
        verbose_name = 'User Admin'
        verbose_name_plural = 'Users Admin'
