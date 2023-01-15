from django import forms

from apps.home import models


class CampaignVenueForm(forms.ModelForm):

    class Meta:
        model = models.Campaign
        fields = ('venues', )


class CampaignForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))
    end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))

    class Meta:
        model = models.Campaign
        fields = ('name', 'start_date', 'end_date', 'venues', 'owner', 'washroom_groups')
        widgets = {
            'venues': forms.Select(attrs={'disabled': 'disabled'}),
        }

    def __init__(self, venue=None, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.fields['washroom_groups'].queryset = models.Washroom.objects.filter(venue=venue)


class CampaignUpdateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))
    end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label='Nothing'))

    class Meta:
        model = models.Campaign
        fields = ('name', 'start_date', 'end_date', 'venues', 'owner', 'washroom_groups')
        # widgets = {
        #     'venues': forms.Select(attrs={'disabled': 'disabled'}),
        #     'washroom_groups': forms.Select(attrs={'disabled': 'disabled'}),
        # }


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
        fields = ('gender', 'name', 'group_association', 'venue', )


class WashroomGroupsForm(forms.ModelForm):
    class Meta:
        model = models.WashroomGroups
        fields = ('washrooms', )


class FaucetForm(forms.ModelForm):
    class Meta:
        model = models.Faucet
        fields = ('name', 'mac', 'ip_address', 'status', 'playlist', 'washroom')


class MediaForm(forms.ModelForm):
    # file = forms.FileField()

    class Meta:
        model = models.Media
        fields = ('name', 'campaign', 'type', 'file', )
