from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Account(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Format: '+999999999'. Max 15 digits.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
