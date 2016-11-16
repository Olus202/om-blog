from django.test import TestCase
from selenium import webdriver


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
        header = self.browser.find_element_by_id('header').text
        self.assertTrue('First post' == header)

        pub_date = self.browser.find_element_by_id('pub_date').text
        self.assertTrue('Nov. 15, 2016' == pub_date)

        post_text = self.browser.find_element_by_id('text').text
        self.assertIn('This is first post', post_text)
