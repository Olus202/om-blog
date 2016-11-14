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
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>outdoor marriage</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

