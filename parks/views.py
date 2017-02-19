from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.core.mail import mail_admins
from .newdata import parse, cleardb
from .forms import ProblemForm
from .models import Park
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'parks/index.html'
    context_object_name = 'list_of_parks'

    def get_context_data(self, **kwargs):
        context = generic.ListView.get_context_data(self, **kwargs)
        context['favorite'] = self.request.GET.get('favorite', None)
        context['washroom'] = self.request.GET.get('washroom', None)
        context['arbutus_ridge'] = self.request.GET.get('arbutus_ridge', None)
        context['downtown'] = self.request.GET.get('downtown', None)
        context['west_end'] = self.request.GET.get('west_end', None)
        context['dunbar_southlands'] = self.request.GET.get('dunbar_southlands', None)
        context['fairview'] = self.request.GET.get('fairview', None)
        context['grandview_woodland'] = self.request.GET.get('grandview_woodland', None)
        context['hastings_sunrise'] = self.request.GET.get('hastings_sunrise', None)
        context['kensington_cedar_cottage'] = self.request.GET.get('kensington_cedar_cottage', None)
        context['kerrisdale'] = self.request.GET.get('kerrisdale', None)
        context['killarney'] = self.request.GET.get('killarney', None)
        context['west_point_grey'] = self.request.GET.get('west_point_grey', None)
        context['kitsilano'] = self.request.GET.get('kitsilano', None)
        context['marpole'] = self.request.GET.get('marpole', None)
        context['mount_pleasant'] = self.request.GET.get('mount_pleasant', None)
        context['oakridge'] = self.request.GET.get('oakridge', None)
        context['south_cambie'] = self.request.GET.get('south_cambie', None)
        context['renfrew_collingwood'] = self.request.GET.get('renfrew_collingwood', None)
        context['riley_little_mountain'] = self.request.GET.get('riley_little_mountain', None)
        context['shaughnessy'] = self.request.GET.get('shaughnessy', None)
        context['strathcona'] = self.request.GET.get('strathcona', None)
        context['sunset'] = self.request.GET.get('sunset', None)
        context['victoria_fraserview'] = self.request.GET.get('victoria_fraserview', None)
        context['map_select'] = self.request.GET.get('map', None)
        return context

    def get_queryset(self):
        queryset = Park.objects.order_by('name')
        neighbourhoods = []
        favorites = []

        # get the filters from the GET
        request_favorite = self.request.GET.get('favorite', None)
        if request_favorite == 'true':
            favorites = get_favorite_parks(self.request)
        request_washroom = self.request.GET.get('washroom', None)
        if request_washroom == 'true':
            queryset = queryset.filter(washroom=1)
        arbutus_ridge = self.request.GET.get('arbutus_ridge', None)
        if arbutus_ridge == 'true':
            neighbourhoods.append('Arbutus Ridge')
        downtown = self.request.GET.get('downtown', None)
        if downtown == 'true':
            neighbourhoods.append('Downtown')
        west_end = self.request.GET.get('west_end', None)
        if west_end == 'true':
            neighbourhoods.append('West End')
        dunbar_southlands = self.request.GET.get('dunbar_southlands', None)
        if dunbar_southlands == 'true':
            neighbourhoods.append('Dunbar-Southlands')
        fairview = self.request.GET.get('fairview', None)
        if fairview == 'true':
            neighbourhoods.append('Fairview')
        grandview_woodland = self.request.GET.get('grandview_woodland', None)
        if grandview_woodland == 'true':
            neighbourhoods.append('Grandview-Woodland')
        hastings_sunrise = self.request.GET.get('hastings_sunrise', None)
        if hastings_sunrise == 'true':
            neighbourhoods.append('Hastings-Sunrise')
        kensington_cedar_cottage = self.request.GET.get('kensington_cedar_cottage', None)
        if kensington_cedar_cottage == 'true':
            neighbourhoods.append('Kensington-Cedar Cottage')
        kerrisdale = self.request.GET.get('kerrisdale', None)
        if kerrisdale == 'true':
            neighbourhoods.append('Kerrisdale')
        killarney = self.request.GET.get('killarney', None)
        if killarney == 'true':
            neighbourhoods.append('Killarney')
        west_point_grey = self.request.GET.get('west_point_grey', None)
        if west_point_grey == 'true':
            neighbourhoods.append('West Point Grey')
        kitsilano = self.request.GET.get('kitsilano', None)
        if kitsilano == 'true':
            neighbourhoods.append('Kitsilano')
        marpole = self.request.GET.get('marpole', None)
        if marpole == 'true':
            neighbourhoods.append('Marpole')
        mount_pleasant = self.request.GET.get('mount_pleasant', None)
        if mount_pleasant == 'true':
            neighbourhoods.append('Mount Pleasant')
        oakridge = self.request.GET.get('oakridge', None)
        if oakridge == 'true':
            neighbourhoods.append('Oakridge')
        south_cambie = self.request.GET.get('south_cambie', None)
        if south_cambie == 'true':
            neighbourhoods.append('South Cambie')
        renfrew_collingwood = self.request.GET.get('renfrew_collingwood', None)
        if renfrew_collingwood == 'true':
            neighbourhoods.append('Renfrew-Collingwood')
        riley_little_mountain = self.request.GET.get('riley_little_mountain', None)
        if riley_little_mountain == 'true':
            neighbourhoods.append('Riley-Little Mountain')
        shaughnessy = self.request.GET.get('shaughnessy', None)
        if shaughnessy == 'true':
            neighbourhoods.append('Shaughnessy')
        strathcona = self.request.GET.get('strathcona', None)
        if strathcona == 'true':
            neighbourhoods.append('Strathcona')
        sunset = self.request.GET.get('sunset', None)
        if sunset == 'true':
            neighbourhoods.append('Sunset')
        victoria_fraserview = self.request.GET.get('victoria_fraserview', None)
        if victoria_fraserview == 'true':
            neighbourhoods.append('Victoria-Fraserview')

        # Apply the filters
        if favorites:
            print(favorites)
            queryset = queryset.filter(park_id__in=favorites)
        if neighbourhoods:
            queryset = queryset.filter(neighbourhood__in=neighbourhoods)
        return queryset


def get_favorite_parks(request):
    favorite_parks = request.user.user_profile.favorite_park
    if favorite_parks is None:
        favorite_parks = [0]
        return favorite_parks
    else:
        list_favorite_parks = favorite_parks.split(',')
        list_favorite_parks = [s.replace(';','') for s in list_favorite_parks]
        list_favorite_parks = filter(None, list_favorite_parks)
        list_favorite_parks = list(map(int, list_favorite_parks))
        return list_favorite_parks


class DetailView(generic.DetailView):
    model = Park
    exclude = ('user',)
    template_name = 'parks/detail.html'
    slug_field = 'park_id'
    slug_url_kwarg = 'park_id'
    helmet = 'cool'


def get_data(request):
    if request.GET.get('getdata'):
        parse()
    return redirect('parks:index')


def clear_data(request):
    if request.GET.get('cleardata'):
        cleardb()
    return redirect('parks:index')


@csrf_exempt
def put_rating(request):

    if request.method == 'PUT':
        response_data = {}
        put = QueryDict(request.body)
        current_user = request.user
        if not current_user.is_authenticated():
            response_data['authenticated'] = False
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        response_data['authenticated'] = True
        rating = put.get('rating')
        pid = put.get('pid')
        park = Park.objects.get(park_id=pid)
        park.update_rating(float(rating), current_user)


        response_data['park_id'] = park.park_id
        response_data['parkname'] = park.name
        response_data['rating'] = park.rating


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse()

@login_required
def add_favorite_park(request, park_id):
    if request.method =='POST':
        user_profile = request.user.user_profile
        favorite_parks = request.user.user_profile.favorite_park
        if favorite_parks is None:
            favorite_parks = ''
        favorite_parks += ";"
        favorite_parks += park_id
        favorite_parks += ";,"
        user_profile.favorite_park = favorite_parks
        user_profile.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def unfavorite_park(request, park_id):
    if request.method =='POST':
        user_profile = request.user.user_profile
        favorite_parks = request.user.user_profile.favorite_park
        if favorite_parks is None:
            favorite_parks = ''
        deleted_park = ";"
        deleted_park += park_id
        deleted_park += ";,"
        new_favorite_parks = favorite_parks.replace(deleted_park, '')
        user_profile.favorite_park = new_favorite_parks
        user_profile.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def submit_problem(request, park_id):
    if request.POST:
        form = ProblemForm(request.POST)
        if form.is_valid():
            my_park = Park.objects.get(park_id=park_id)
            username = request.user.get_username()
            description = form.cleaned_data['description']
            mail_admins('Problem with '+ my_park.name, "Park: " + my_park.name + "\nPark ID: " + park_id + "\nDescription of Problem: " + description + "\nSubmitted by user: " + username)
            print("form was valid")
            print(description)
        else:
            print("form was invalid")

    return redirect('parks:problem_done')