from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from apps.home import models, utils
from users.models import Account


@login_required(login_url="/login/")
def update(request, model, pk):
    loader_template = loader.get_template('layouts/update-record.html')
    instance = get_object_or_404(utils.get_model_from_segment(model), id=pk)
    form_object = utils.get_form_from_segment(model)

    if request.method == 'POST':
        form = form_object(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse(model))

    form = form_object(instance=instance)
    context = {
        'segment': model,
        'form': form
    }
    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def create_new_record(request, model):
    if not model:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        form_object = utils.get_form_from_segment(model)
        form = form_object(request.POST)

        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse(model))


@login_required(login_url="/login/")
def new_record(request, model):
    loader_template = loader.get_template('layouts/add-new-record.html')
    context = {
        'segment': model,
        'form': utils.get_form_from_segment(model)
    }
    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def delete(request, model, pk):
    if not model:
        return HttpResponseRedirect(reverse('index'))

    model_object = utils.get_model_from_segment(model)
    record_to_delete = model_object.objects.get(id=pk)

    if record_to_delete:
        record_to_delete.delete()

    return HttpResponseRedirect(reverse(model))


@login_required(login_url="/login/")
def profile(request):
    html_template = loader.get_template('home/page-user.html')
    context = {'segment': 'page-user'}
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def administration(request):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []
    table_records = {}

    if request.method == 'GET':
        for a in Account.objects.all():
            table_records['col1'] = a.email
            table_records['col2'] = a.is_staff
            table_records['col3'] = a.date_created
            table_records['col4'] = a.is_active
            table_records['Action'] = a.id
            table_body.append(table_records.copy())

    context = {
        'segment': 'administration',
        'table_header': ['Username', 'AVNO', 'Date Created', 'Active', 'Action'],
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def reporting(request):
    html_template = loader.get_template('home/ui-notifications.html')
    context = {'segment': 'reporting'}
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def media(request):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []
    table_records = {}

    if request.method == 'GET':
        for m in models.Media.objects.all():
            table_records['col1'] = m.name
            table_records['col2'] = m.date_uploaded
            table_records['col3'] = m.type
            table_records['col4'] = m.size
            table_records['Action'] = m.id
            table_body.append(table_records.copy())

    context = {
        'segment': 'media',
        'table_header': ['Media Name', 'Date Uploaded', 'Type', 'Size', 'Action'],
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def faucets(request):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []
    table_records = {}

    if request.method == 'GET':
        for f in models.Faucet.objects.all():
            table_records['col1'] = f.name
            table_records['col2'] = f.mac
            table_records['col3'] = f.ip_address
            table_records['col4'] = f.status
            table_records['Action'] = f.id
            table_body.append(table_records.copy())

    context = {
        'segment': 'faucets',
        'table_header': ['Faucet Name', 'MAC', 'IP Address', 'Status', 'Action'],
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def venues(request):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []
    table_records = {}

    if request.method == 'GET':
        for v in models.Venue.objects.all():
            table_records['col1'] = v.name
            table_records['col2'] = v.country
            table_records['col3'] = v.state
            table_records['Action'] = v.id
            table_body.append(table_records.copy())

    context = {
        'segment': 'venues',
        'table_header': ['Venue Name', 'Country', 'State', 'Action'],
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def campaigns(request):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []
    table_records = {}

    if request.method == 'GET':
        all_campaigns = models.Campaign.objects.all()
        for c in all_campaigns:
            table_records['col1'] = c.name
            table_records['col2'] = c.start_date
            table_records['col3'] = c.end_date
            table_records['Action'] = c.id
            table_body.append(table_records.copy())

    if request.method == 'POST':
        pass

    context = {
        'segment': 'campaigns',
        'table_subtitle': '',
        'table_header': ['Campaign Name', 'Date Created', 'Date Expires', 'Action'],
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print(str(e))
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
