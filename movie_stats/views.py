from django.shortcuts import render, get_object_or_404
from .models import Movie
from forms import MovieForm
from django.shortcuts import redirect

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

def new_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(all_statistics, post.pk)
    else:
        form = MovieForm()
    return render(request, 'movieform.html', {'form': form})