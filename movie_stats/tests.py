from django.test import TestCase
from movie_stats.views import all_statistics
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from models import Movie

class MovieStatsViewTest(TestCase):

# Check that the URL resolves
    def test_movie_page_resolves(self):
        movie_page = resolve('/stats/')
        self.assertEqual(movie_page.func, all_statistics)

# Check that the correct template & movie content rendered
    def test_check_movie_content_is_correct(self):
        movie_page = self.client.get('/stats/')
        self.assertTemplateUsed(movie_page, "movie_stats.html")
        movie_page_template_output = render_to_response("movie_stats.html",
                                                        {'movies':
Movie.objects.all()}).content
        self.assertEqual(movie_page.content, movie_page_template_output)