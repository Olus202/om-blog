from django.test import TestCase
from selenium import webdriver


class RunningBlog(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_run_main(self):
        # Run the page
        self.browser.get('http://127.0.0.1:8000/')

        # Assert if 'Django' in title
        self.assertIn('Django', self.browser.title)

