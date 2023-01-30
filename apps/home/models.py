from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # TODO: Según el PDF, esto es un ManyToMany
    venues = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True)

    # TODO: Según el PDF, esto es un ManyToMany
    washroom_groups = models.ForeignKey(
        'WashroomGroups', on_delete=models.CASCADE, null=True, related_name='campaigns', blank=True)
    owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) if self.name else "-"

    def get_media(self):
        return self.media_files.all()

    def get_media_urls(self):
        all_urls = []
        for m in self.get_media():
            all_urls.append(getattr(settings, 'HOSTNAME') + m.file.url)

        return all_urls


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True, null=True)

    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    playlist = models.IntegerField(
        default=0, blank=True, null=True,
        help_text='This field is auto-filled with the number of related Campaigns'
    )
    ad_approver = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField("email address", blank=True, null=True)

    contract_start = models.DateField(blank=True, null=True)
    contract_end = models.DateField(blank=True, null=True)

    loop_size = models.IntegerField(default=0)
    max_ad_time = models.TimeField(blank=True, null=True)

    owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) if self.name else "-"


class WashroomGroups(models.Model):
    name = models.CharField(max_length=100, default="Washroom Group v1")
    # washrooms = models.ManyToManyField(to='Washroom', related_name='washroom_group')

    class Meta:
        verbose_name = "Washroom Group"
        verbose_name_plural = "Washroom Groups"

    def __str__(self):
        return "(" + self.name + ")" + " " + self.get_washrooms()

    def get_washrooms(self):
        wlist = []
        if len(self.washrooms.all()) > 0:
            wlist = [f.name for f in self.washrooms.all()]
        wc = wlist if wlist else "not assigned"
        return str(wc)


class Washroom(models.Model):
    GENDERS = (
        ('FAMILY', 'Family'),
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
    GENDERS_DEFAULT = 'FAMILY'

    gender = models.CharField(
        max_length=25,
        choices=GENDERS,
        default=GENDERS_DEFAULT
    )
    name = models.CharField(max_length=100)
    washroom_groups = models.ForeignKey(
        WashroomGroups, models.CASCADE, null=True, blank=True, related_name="washrooms")
    venues = models.ForeignKey(
        'Venue', on_delete=models.CASCADE, related_name='washrooms', null=True)

    def __str__(self):
        return str(self.name) if self.name else "-"


class Faucet(models.Model):
    STATUS = (
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
    )
    STATUS_DEFAULT = 'OFFLINE'

    name = models.CharField(max_length=100, blank=True, null=True)
    mac = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        choices=STATUS, default=STATUS_DEFAULT,
        max_length=50, blank=True, null=True
    )
    playlist = models.CharField(max_length=100, blank=True, null=True)

    washroom = models.ForeignKey(
        'Washroom', on_delete=models.CASCADE, related_name='faucets', null=True)

    def __str__(self):
        return str(self.name) if self.name else "-"


class Media(models.Model):
    TYPE = (
        ('VIDEO', 'Video'),
        ('PHOTO', 'Photo'),
    )
    TYPE_DEFAULT = 'VIDEO'

    name = models.CharField(max_length=100)

    file = models.FileField(upload_to='media/', null=True, blank=True)

    campaign = models.ForeignKey(
        "Campaign", on_delete=models.CASCADE, null=True, related_name="media_files")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=25,
        choices=TYPE,
        default=TYPE_DEFAULT
    )

    def __str__(self):
        return str(self.name) if self.name else "-"
