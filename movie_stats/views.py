from django.shortcuts import render, get_object_or_404
from .models import Movie

def all_statistics(request):
    movies = Movie.objects.order_by('-id')
    return render(request, "movie_stats.html", {"movies": movies})

def review_detail(request, id):
    """
    Create a view that returns a single
    Review object based on the ID and
    and render it to the 'review.html'
    template. Or return a 404 error if the
    post is not found
    """

    review = get_object_or_404(Movie, pk=id)
    return render(request, "review.html", {'review': review})