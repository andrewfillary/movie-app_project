from django.test import TestCase
from Hello.views import get_magazine_and_review
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from movie_stats.models import Movie

class HelloViewTest(TestCase):

# Check that the URL resolves
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_magazine_and_review)

# Check that the correct template & movie content rendered
    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html",
                                                        {'movies':
Movie.objects.order_by('id')[:1]}).content
        self.assertEqual(home_page.content, home_page_template_output)