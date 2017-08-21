from django.db import models

RATINGS = (
    ('Must see', 'Must see'),
    ('Worth a watch', 'Worth a watch'),
    ('B Movie', 'B Movie'),
)

GENRES = (
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Romance', 'Romance'),
    ('Thriller', 'Thriller'),
    ('Sci Fi', 'Sci Fi')
)
class Movie(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    review = models.TextField()
    cover_art = models.ImageField(upload_to="images", blank=True, null=True)
    screen_image = models.ImageField(upload_to="images", blank=True, null=True)
    rating = models.CharField(max_length=15, choices=RATINGS, default='Smash hit')
    percentage = models.CharField(max_length=3, blank=True, null=True)
    box_office = models.CharField(max_length=15, blank=True, null=True)
    budget = models.CharField(max_length=15, blank=True, null=True)
    opening_weekend = models.CharField(max_length=15, blank=True, null=True)
    director = models.CharField(max_length=20, blank=True, null=True)
    actors = models.CharField(max_length=100, blank=True, null=True)
    theatre_release = models.CharField(max_length=10, blank=True, null=True)
    dvd_release = models.CharField(max_length=10, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    genre = models.CharField(max_length=8, choices=GENRES, default='Action')