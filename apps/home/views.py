from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from apps.home import utils
from apps.home.forms import CampaignVenueForm
from apps.home.models import Campaign


@login_required(login_url="/login/")
def show(request, model):
    html_template = loader.get_template('layouts/base-tables.html')
    table_body = []

    if request.method == 'GET':
        cobjects = utils.get_objects_from_segment(model, request.user)
        table_body = utils.get_table_body_from_objects(cobjects, model)

    context = {
        'segment': model,
        'table_subtitle': '',
        'table_header': utils.get_header_from_segment(model),
        'table_body': table_body,
    }

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def update(request, model, pk):
    loader_template = loader.get_template('layouts/update-record.html')
    instance = get_object_or_404(utils.get_model_from_segment(model), id=pk)

    form_object = utils.get_form_from_segment(model)

    if request.method == 'POST':
        form = form_object(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('show_model', kwargs={'model': model}))

    form = form_object(instance=instance)
    context = {
        'segment': model,
        'form': form
    }
    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def create_new_campaign(request, model):
    loader_template = loader.get_template('layouts/add-campaign.html')
    form_object = CampaignVenueForm

    if request.method == 'GET':
        context = {
            'segment': model,
            'form': form_object
        }
    else:
        form = form_object(request.POST)

        if form.is_valid():
            campaign = form.save(commit=False)
            venue = campaign.venues.id

            return HttpResponseRedirect(reverse('add_new_record', kwargs={
                'model': model, 'venue': venue}))
        else:
            context = {
                'segment': model,
                'form': form
            }

    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def create_new_record(request, model, venue=None):
    loader_template = loader.get_template('layouts/add-new-record.html')
    form_object = utils.get_form_from_segment(model, venue=venue)

    if request.method == 'GET':
        context = {
            'segment': model,
            'form': form_object,
            'venue': venue
        }
    else:
        if request.FILES:
            form = form_object(request.POST, request.FILES)
        elif venue:
            form = form_object(request.POST)
            instance = form.save(commit=False)
            instance.venues = venue
            instance.save()
        else:
            form = form_object(request.POST)

        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            # messages.success(request, 'user_admin with name {} added.'.format(user.username))
            return HttpResponseRedirect(reverse('show_model', kwargs={'model': model}))
        else:
            context = {
                'segment': model,
                'form': form
            }

    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def delete(request, model, pk):
    model_object = utils.get_model_from_segment(model)
    record_to_delete = model_object.objects.get(id=pk)

    if record_to_delete:
        record_to_delete.delete()

    return HttpResponseRedirect(reverse('show_model', kwargs={'model': model}))


@login_required(login_url="/login/")
def profile(request):
    html_template = loader.get_template('home/page-user.html')
    context = {'segment': 'page-user'}
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def reporting(request):
    html_template = loader.get_template('home/ui-notifications.html')
    context = {'segment': 'reporting'}
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
