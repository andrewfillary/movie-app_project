from django.test import TestCase
from Hello.views import get_magazine_and_review
from django.core.urlresolvers import resolve

class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_magazine_and_review)
