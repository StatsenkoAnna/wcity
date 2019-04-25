from django.test import TestCase
from django.test import Client
from .models import Fenster
from django.http import HttpResponse

# Create your tests here.

class FensterTest(TestCase):
    def setup(self):
        self.client = Client()
        f = Fenster(
            fenster_width = 10
            )
    
    def test_buy(self):
        response = self.client.post('/fenster/buy/',
                                    {
                                        'selected_fenster' : '10'
                                    }
                                    )
        self.assertIsInstance(response, HttpResponse)

    def test_index(self):
        pass
        
