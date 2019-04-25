from xml.etree import ElementTree as ET

import mock
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import Storage

from ..models import KasaDakaUser, CallSession, CallSessionStep
from ..models import VoiceService, Choice, ChoiceOption
from ..models import Language, VoiceLabel, VoiceFragment

from .helpers import create_sample_voice_service

class TestChoiceView(TestCase):
    client = Client()
    caller_id = "1234"

    def setUp(self):
       create_sample_voice_service(self)
        

    def test_choice_vxml(self):
        response = self.client.get(self.choice_url)
        assert response.status_code == 200
        assert ET.fromstring(response.content), 'Should produce valid XML'
