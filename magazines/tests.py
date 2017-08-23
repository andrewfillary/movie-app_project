from django.test import TestCase
from magazines.views import all_magazines
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from models import Magazine

class MagazineViewTest(TestCase):

 # Check that the URL resolves
    def test_magazine_page_resolves(self):
        magazine_page = resolve('/magazines/')
        self.assertEqual(magazine_page.func, all_magazines)

# Check that the correct template & magazine content rendered
    def test_check_magazine_content_is_correct(self):
        magazine_page = self.client.get('/magazines/')
        self.assertTemplateUsed(magazine_page, "magazines/magazines.html")
        magazine_page_template_output = render_to_response("magazines/magazines.html",
                                                            {'magazines':
Magazine.objects.all()}).content
        self.assertEqual(magazine_page.content, magazine_page_template_output)