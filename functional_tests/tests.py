import datetime
from django.test import TestCase
from selenium import webdriver

from blog.models import Post


class VisitBlog(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_of_home_page(self):
        # Check title
        self.assertIn('outdoor marriage', self.browser.title)

    def test_content_of_home_page(self):
        # Check header, publication date and text in home.html
        first_post = Post()
        first_post.text = "This is first post"
        first_post.pub_date = "2016-11-16"
        first_post.header = "First post"
        first_post.save()

        post = Post.objects.all()[0]

        header = self.browser.find_element_by_id('header').text
        self.assertTrue(post.header == header)

        pub_date = self.browser.find_element_by_id('pub_date').text
        self.assertTrue(str(post.pub_date) == pub_date)

        post_text = self.browser.find_element_by_id('text').text
        self.assertIn(post.text, post_text)
