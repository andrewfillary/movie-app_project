from django.shortcuts import render
from magazines.models import Magazine
from movie_stats.models import Movie

def get_magazine_and_review(request):
    magazines = Magazine.objects.order_by('id')[:1]
    movies = Movie.objects.order_by('id')[:1]
    return render(request, "index.html", {"magazines": magazines, "movies": movies })


