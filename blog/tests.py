import datetime
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import home_page
from blog.models import Post


class HomePageTest(TestCase):

    def test_check_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_to_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class PostModelTest(TestCase):

    def test_saving_and_retrieving_post(self):
        first_post = Post()
        first_post.text = "This is first post"
        first_post.pub_date = datetime.date.today()
        first_post.header = "First post"
        first_post.save()

        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 1)

        saved_post = saved_posts[0]
        self.assertEqual(saved_post.text, 'This is first post')
        self.assertEqual(saved_post.pub_date, datetime.date.today())
        self.assertEqual(saved_post.header, 'First post')






