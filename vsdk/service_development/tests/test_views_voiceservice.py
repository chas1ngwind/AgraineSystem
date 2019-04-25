from xml.etree import ElementTree as ET

import mock
import random
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import Storage

from ..models import KasaDakaUser, CallSession, CallSessionStep
from ..models import VoiceService, Choice, ChoiceOption
from ..models import Language, VoiceLabel, VoiceFragment

from .helpers import create_sample_voice_service

class TestVoiceServiceView(TestCase):
    client = Client()
    caller_id = "1234"

    def setUp(self):
        create_sample_voice_service(self)
        self.voice_service_urls_name = self.voice_service._urls_name 
        self.voice_service_url = reverse(self.voice_service_urls_name,
                kwargs = {'voice_service_id': self.voice_service.id})
        self.voice_service_url_plus_session = reverse(self.voice_service_urls_name,
                kwargs = {'voice_service_id': self.voice_service.id,
                    'session_id': self.session.id})

    def test_voice_service_start_without_session_known_callerid(self):
        """
        If the CallerID is provided which has a registered user, but not the session_id,
        a new session should be created and the user redirected to the starting element
        of the voice service.
        """
        self.voice_service.requires_registration = True
        self.voice_service.save()

        response = self.client.get(self.voice_service_url,
                {'callerid': self.caller_id})
        
        new_session_id = CallSession.objects.all().filter(user = self.user).order_by('-start')[0].id
        expected_redirection_url = reverse(self.voice_service.start_element._urls_name,
                kwargs = {'element_id': self.voice_service.start_element.id,
                    'session_id': new_session_id})
        self.assertRedirects(response,expected_redirection_url)

    def test_voice_service_start_without_session_unknown_callerid(self):
        """
        If the CallerID that is provided is not known,
        user should be sent to registration form.
        """
        caller_id =  str(random.randint(100000,999999))
        response = self.client.get(self.voice_service_url,
                {'callerid': caller_id})
        session = CallSession.objects.all().order_by('-start')[0]
        session_id = session.id
        assert session.caller_id == caller_id


        self.assertRedirects(response,reverse('service-development:user-registration')+"?caller_id="+str(caller_id)+"&session_id="+str(session_id))

    def test_voice_service_start_without_session_without_callerid_registration_not_required(self):
        """
        When no callerid is provided, the user should only be redirected to the
        language selection form (temporary for this session), when the
        voice service does not require registration, and has more than one supported
        language.
        """
        self.voice_service.requires_registration = False
        self.voice_service.supported_languages.add(self.language2)
        self.voice_service.save()

        response = self.client.get(self.voice_service_url)
        session = CallSession.objects.all().order_by('-start')[0]
        session_id = session.id
        assert session.caller_id == None
        expected_redirection_url = reverse('service-development:language-selection',
            kwargs = {'voice_service_id': self.voice_service.id,
            'session_id': session_id})
        self.assertRedirects(response, expected_redirection_url)

    def test_voice_service_start_without_session_without_callerid_registration_required(self):
        """
        When no callerid is provided, and service requires registration,
        an error should be presented.
        """
        self.voice_service.requires_registration = True
        self.voice_service.save()
        with self.assertRaises(ValueError) as ve:
            response = self.client.get(self.voice_service_url)

    def test_voice_service_start_with_session_id(self):
        """
        If the session is provided, and is valid:
        - Has an user if registration is required
        - Has a language that is valid for the voice service
        Redirect the user to the starting element of the voice service.
        """
        self.voice_service.requires_registration = False
        self.voice_service.supported_languages.add(self.language2)
        self.voice_service.save()
        session = CallSession.objects.create(user = None, service=self.voice_service,
                _language = self.language) 
        url = reverse(self.voice_service_urls_name,
                kwargs = {'voice_service_id': self.voice_service.id,
                    'session_id': session.id})
        
        response = self.client.get(url)
        expected_redirection_url = reverse(self.voice_service.start_element._urls_name,
                kwargs = {'element_id': self.voice_service.start_element.id,
                    'session_id': session.id})
        self.assertRedirects(response,expected_redirection_url)

    
