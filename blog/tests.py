from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page


class HomePageTest(TestCase):

    def test_check_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_to_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
