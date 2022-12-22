from apps.home import models, forms
from users.forms import UserAdminForm, AvnoAdminForm
from users.models import Account, UserAdmin as admin_user


def get_table_records_from_object(obj, segment):
    table_records = {}

    if segment == 'campaigns':
        table_records['col1'] = obj.name
        table_records['col2'] = obj.start_date
        table_records['col3'] = obj.end_date
    if segment == 'venues':
        table_records['col1'] = obj.name
        table_records['col2'] = obj.country
        table_records['col3'] = obj.state
    if segment == 'washrooms':
        table_records['col1'] = obj.gender
        table_records['col2'] = obj.name
        table_records['col3'] = obj.group_association
        faucets_list = []
        if len(obj.faucets.all()) > 0:
            faucets_list = [f.name for f in obj.faucets.all()]
        faucets = faucets_list if faucets_list else "not assigned"
        table_records['col4'] = faucets
    if segment == 'faucets':
        table_records['col1'] = obj.name
        table_records['col2'] = obj.mac
        table_records['col3'] = obj.ip_address
        table_records['col4'] = obj.status
    if segment == 'media':
        table_records['col1'] = obj.name
        table_records['col2'] = obj.date_uploaded
        table_records['col3'] = obj.type
        table_records['col4'] = obj.file.size if obj.file else 0
    if segment == 'user-admin':
        table_records['col1'] = obj.username
        table_records['col2'] = obj.email
        table_records['col3'] = obj.avno_user
        table_records['col4'] = obj.is_active
        table_records['col5'] = obj.date_created
    if segment == 'avno-admin':
        table_records['col1'] = obj.username
        table_records['col2'] = obj.email
        table_records['col3'] = obj.is_avno
        table_records['col4'] = obj.is_active
        table_records['col5'] = obj.date_created

    table_records['Action'] = obj.id

    return table_records


def get_table_body_from_objects(cobjects, segment):
    table_body = []

    for c in cobjects:
        table_records = get_table_records_from_object(c, segment)
        table_body.append(table_records.copy())

    return table_body


def get_objects_from_segment(segment, user):
    model = get_model_from_segment(segment)
    if user.is_avno:
        return model.objects.all()

    try:
        avno = admin_user.objects.get(id=user.id)
    except admin_user.DoesNotExist:
        raise Exception("There was a problem with your user grants. Please, "
                        "contact an admin person to solve this problem.")

    try:
        avno_username = avno.avno_user
    except AttributeError:
        raise Exception("This user needs an AVNO user to be assigned.")

    if segment in ['campaigns', 'venues', 'media']:
        return model.objects.filter(owner__username=avno_username)
    if segment in ['washrooms']:
        return model.objects.filter(campaigns__owner__username=avno_username)
    if segment in ['faucets']:
        return model.objects.filter(washrooms__campaigns__owner__username=avno_username)


def get_header_from_segment(segment=None):
    if segment == 'campaigns':
        return ['Campaign Name', 'Date Created', 'Date Expires', 'Action']
    if segment == 'venues':
        return ['Venue Name', 'Country', 'State', 'Action']
    if segment == 'washrooms':
        return ['Gender', 'Name', 'Group Association', 'Faucets', 'Action']
    if segment == 'faucets':
        return ['Faucet Name', 'MAC', 'IP Address', 'Status', 'Action']
    if segment == 'media':
        return ['Media Name', 'Date Uploaded', 'Type', 'Size', 'Action']
    if segment in ['user-admin', 'avno-admin']:
        return ['Username', 'Email', 'AVNO', 'Active', 'Date Created', 'Action']


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
    if segment == 'user-admin':
        return admin_user
    if segment == 'avno-admin':
        return Account


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
    if segment == 'user-admin':
        return UserAdminForm
    if segment == 'avno-admin':
        return AvnoAdminForm
