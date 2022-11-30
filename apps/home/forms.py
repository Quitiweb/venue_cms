from django import forms

from apps.home import models


class CampaignForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))
    end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))

    class Meta:
        model = models.Campaign
        fields = ('name', 'start_date', 'end_date', 'venues', 'washroom_groups',
                  'media', 'owner')


class VenueForm(forms.ModelForm):
    contract_start = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))
    contract_end = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))

    class Meta:
        model = models.Venue
        fields = (
            'name', 'address1', 'address2', 'country', 'state', 'city',
            'owner', 'ad_approver', 'phone', 'email', 'contract_start',
            'contract_end', 'loop_size'
        )


class WashroomForm(forms.ModelForm):
    class Meta:
        model = models.Washroom
        fields = ('gender', 'name', 'group_association', 'faucets')


class FaucetForm(forms.ModelForm):
    class Meta:
        model = models.Faucet
        fields = ('name', 'mac', 'ip_address', 'status', 'playlist')


class MediaForm(forms.ModelForm):

    class Meta:
        model = models.Media
        fields = ('name', 'type', 'size')
