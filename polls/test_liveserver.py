from django.test import LiveServerTestCase
from django.test import Client

"""checks that the polls page loads successfully when accessed from the live server"""
class PollsLiveServerTests(LiveServerTestCase):
    def test_polls_page_loads_on_live_server(self):
        client = Client()
        response = client.get(f"{self.live_server_url}/polls/")
        self.assertEqual(response.status_code, 200)