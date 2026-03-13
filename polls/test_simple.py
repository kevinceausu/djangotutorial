from django.test import SimpleTestCase
from django.urls import reverse

"""tests that the polls index URL uses correctly the reverse() function"""
class PollsSimpleTests(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("polls:index")
        self.assertEqual(url, "/polls/")