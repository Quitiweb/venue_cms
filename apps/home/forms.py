from django import forms

from apps.home import models


class CampaignsForm(forms.ModelForm):

    class Meta:
        model = models.Campaign
        fields = ('name', 'start_date', 'end_date')
