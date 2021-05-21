from django.http import HttpResponse
from django.template import loader
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .graph import graph_test, get_path, graph_test_2, get_path_2, start_timer, stop_timer, print_values
from .models import Station, Ligne, Trajet
from .forms import TrajetForm

def search_trajet_1(depart,arrive):
    path_distance, path_list = get_path(depart,arrive)

    return path_distance, path_list

def search_trajet_2(depart,arrive):
    destination, predecessor = get_path_2(depart,arrive)
    #destination, predecessor = graph_test_2()

    return destination, predecessor

def index(request):
    connect = False
    if request.user.is_authenticated:
        connect = True

    template = loader.get_template('index.html')
    stations = Station.objects.all().order_by('nom')

    form = TrajetForm()

    context = {
        'stations'  : stations,
        'form'      : form,
        'connect'   : connect
    }

    return HttpResponse(template.render(context, request))

def stations_view(request):
    template = loader.get_template('stations.html')
    list_stations = Station.objects.all().order_by('nom')

    context = {
        'list_stations': list_stations,
    }

    return HttpResponse(template.render(context, request))

def lignes_view(request):
    template = loader.get_template('lignes.html')
    list_lignes = Ligne.objects.all().order_by('nom')

    context = {
        'list_lignes': list_lignes,
    }

    return HttpResponse(template.render(context, request))

def trajet_view(request):
    template = loader.get_template('trajet.html')

    if request.method == 'POST':
        form = TrajetForm(request.POST)
        if form.is_valid():
            depart = Station.objects.get(pk=form.cleaned_data['depart'])
            arrive = Station.objects.get(pk=form.cleaned_data['arrive'])

            start_1                 = start_timer()
            distance, trajet_1      = search_trajet_1(depart,arrive)
            time_1                  = stop_timer(start_1)

            start_2                 = start_timer()
            trajet_2, predecesseur  = search_trajet_2(depart,arrive)
            time_2                  = stop_timer(start_2)

            values                  = print_values()

            context = {
                'depart'    : depart,
                'arrive'    : arrive,
                'trajet_1'  : trajet_1,
                'time_1'    : time_1,
                'trajet_2'  : trajet_2,
                'time_2'    : time_2,
                'values'    : values
            }

            return HttpResponse(template.render(context, request))

    return HttpResponse(template.render({}, request))

@login_required(login_url='/admin/')
def logout_view(request):
    logout(request)

    template = loader.get_template('logout.html')
    return HttpResponse(template.render({}, request))