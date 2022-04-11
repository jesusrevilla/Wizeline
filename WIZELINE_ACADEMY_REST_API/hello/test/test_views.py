


from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/index.html')

    def test_external_GET(self):
        response = self.client.get(reverse('external'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/external.html')