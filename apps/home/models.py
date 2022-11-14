from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    media_file = models.FileField(blank=True, null=True)
    venues = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True)
    washroom_groups = models.ForeignKey('Washroom', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), on_delete=models.CASCADE)


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True, null=True)

    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    playlist = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), on_delete=models.CASCADE)

    ad_approver = models.CharField(max_length=100, blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Format: '+999999999'. Max 15 digits.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField("email address", blank=True, null=True)

    contract_start = models.DateField(blank=True, null=True)
    contract_end = models.DateField(blank=True, null=True)

    loop_size = models.IntegerField(default=0)
    max_ad_time = models.TimeField(blank=True, null=True)


class Washroom(models.Model):
    gender = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    group_association = models.CharField(max_length=50)
    faucets = models.ForeignKey('Faucet', on_delete=models.CASCADE)


class Faucet(models.Model):
    name = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    playlist = models.CharField(max_length=100)


class Media(models.Model):
    name = models.CharField(max_length=100)
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    size = models.IntegerField(null=True)