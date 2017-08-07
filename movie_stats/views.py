from django.shortcuts import render
from .models import Statistic

def all_statistics(request):
    statistics = Statistic.objects.all()
    return render(request, "movie_stats.html", {"statistics": statistics})

