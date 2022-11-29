from apps.home import models, forms


def get_model_from_segment(segment=None):
    if segment == 'campaigns':
        return models.Campaign
    if segment == 'venues':
        return models.Venue
    if segment == 'washrooms':
        return models.Washroom
    if segment == 'faucets':
        return models.Faucet
    if segment == 'media':
        return models.Media


def get_form_from_segment(segment=None):
    if segment == 'campaigns':
        return forms.CampaignForm
    if segment == 'venues':
        return forms.VenueForm
    if segment == 'washrooms':
        return forms.WashroomForm
    if segment == 'faucets':
        return forms.FaucetForm
    if segment == 'media':
        return forms.MediaForm
