from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from apps.home import utils


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

    form_object = utils.get_update_form_from_segment(model)

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
    if model == 'campaigns':
        context['media'] = [m for m in instance.media_files.all()]

    return HttpResponse(loader_template.render(context, request))


@login_required(login_url="/login/")
def create_new_record(request, model):
    loader_template = loader.get_template('layouts/add-new-record.html')
    form_object = utils.get_form_from_segment(model)

    if request.method == 'GET':
        context = {
            'segment': model,
            'form': form_object,
        }
    else:
        if request.FILES:
            form = form_object(request.POST, request.FILES)
        else:
            form = form_object(request.POST)

            # Para el formato del user password
            if model == 'user-admin' or model == 'avno-admin':
                data = form.data
                _mutable = data._mutable  # remember old state
                data._mutable = True  # set to mutable

                password = form["password"].value()
                data["password"] = make_password(password)

                data._mutable = _mutable  # set mutable flag back

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
    context = {
        'segment': 'page-user',
        'current_user': request.user,
    }
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
