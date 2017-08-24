from django import forms
from models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'review', 'cover_art', 'screen_image', 'rating', 'percentage', 'box_office',
                  'budget', 'opening_weekend', 'director', 'actors', 'theatre_release', 'dvd_release',
                  'year', 'genre')