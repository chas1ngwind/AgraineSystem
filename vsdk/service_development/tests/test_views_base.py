from xml.etree import ElementTree as ET

import mock

from django.test.utils import setup_test_environment
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import Storage


class TestBaseView(TestCase):
    client = Client()

    def setUp(self):
        pass

    def test_index_page(self):
        url = reverse('service-development:index')
        resp = self.client.get(url)
        assert resp.status_code == 200

        

