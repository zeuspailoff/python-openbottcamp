from django.shortcuts import render
from .models import *


def index(request):
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()
    num_director = Director.objects.all().count()

    available = MovieInstance.objects.filter(status__exact='D').count()

    return render(
        request,
        'index.html',

        context={
            'num_director': num_director,
            'num_movies': num_movies,
            'num_instances': num_instances,
            'available': available
        }
    )


def movies(request):
    return render(
        request,
        'movies.html',
    )
