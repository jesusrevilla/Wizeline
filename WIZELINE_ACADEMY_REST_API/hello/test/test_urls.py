from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hello.views import index, external

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_external_url_resolves(self):
        url = reverse('external')
        self.assertEquals(resolve(url).func, external)