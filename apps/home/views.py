from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.home import forms, models


@login_required(login_url="/login/")
def profile(request):
    plantilla = loader.get_template('home/page-user.html')
    context = {'segment': 'page-user'}
    return HttpResponse(plantilla.render(context, request))


@login_required(login_url="/login/")
def reporting(request):
    plantilla = loader.get_template('home/ui-notifications.html')
    context = {'segment': 'reporting'}
    return HttpResponse(plantilla.render(context, request))


@login_required(login_url="/login/")
def media(request):
    plantilla = loader.get_template('layouts/base-tables.html')
    table_body = []

    if request.method == 'GET':
        for m in models.Media.objects.all():
            table_body.append([m.name, m.date_uploaded, m.type, m.size])

    context = {
        'segment': 'media',
        'table_title': 'Media',
        'table_subtitle': '',
        'table_header': ['Media Name', 'Date Uploaded', 'Type', 'Size'],
        'table_body': table_body,
    }

    return HttpResponse(plantilla.render(context, request))


@login_required(login_url="/login/")
def faucets(request):
    plantilla = loader.get_template('layouts/base-tables.html')
    table_body = []

    if request.method == 'GET':
        for f in models.Faucet.objects.all():
            table_body.append([f.name, f.mac, f.ip_address, f.status])

    context = {
        'segment': 'faucets',
        'table_title': 'Faucets',
        'table_subtitle': '',
        'table_header': ['Faucet Name', 'MAC', 'IP Address', 'Status'],
        'table_body': table_body,
    }

    return HttpResponse(plantilla.render(context, request))


@login_required(login_url="/login/")
def venues(request):
    plantilla = loader.get_template('layouts/base-tables.html')
    table_body = []

    if request.method == 'GET':
        for v in models.Venue.objects.all():
            table_body.append([v.name, v.country, v.state])

    context = {
        'segment': 'venues',
        'table_title': 'Venues',
        'table_subtitle': '',
        'table_header': ['Venue Name', 'Country', 'State'],
        'table_body': table_body,
    }

    return HttpResponse(plantilla.render(context, request))


@login_required(login_url="/login/")
def campaigns(request):
    plantilla = loader.get_template('layouts/base-tables.html')
    table_body = []

    if request.method == 'GET':
        all_campaigns = models.Campaign.objects.all()
        for c in all_campaigns:
            table_body.append([c.name, c.start_date, c.end_date])

    if request.method == 'POST':
        pass

    context = {
        'segment': 'campaigns',
        'table_title': 'Campaigns',
        'table_subtitle': '',
        'table_header': ['Campaign Name', 'Date Created', 'Date Expires'],
        'table_body': table_body,
    }

    return HttpResponse(plantilla.render(context, request))


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
