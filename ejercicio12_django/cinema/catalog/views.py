from django.shortcuts import render
from django.views import generic

from .models import Film, Director, FilmInstance, Genre, Cast, Language
# Create your views here.

def index(request):
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_instaces_available = FilmInstance.objects.filter(status__exact = 'c').count()
    num_director = Director.objects.count()

    return render(
        request,
        'index.html', 
        context=
        {'num_films':num_films, 'num_instances':num_instances, 'num_instances_available':num_instaces_available, 'num_director': num_director}
    )

class FilmListView(generic.ListView):
    model = Film
    context_object_name = 'film_list'
#   # queryset = Film.objects.filter(title__icontains='El padrino')[:5]
#    template_name = 'film_list.html'

class FilmDetailView(generic.DetailView):
    model = Film

class DirectorListView(generic.ListView):
    model = Director
    context_object_name = 'director_list'

class DirectorDetailView(generic.DetailView):
    model = Director