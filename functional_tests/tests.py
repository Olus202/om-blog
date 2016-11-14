from django.test import TestCase
from selenium import webdriver


class VisitBlog(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_run_main(self):
        # Run the page
        self.browser.get('http://127.0.0.1:8000/')

        # Check title
        self.assertIn('outdoor marriage', self.browser.title)

