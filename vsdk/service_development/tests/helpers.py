from xml.etree import ElementTree as ET

import mock
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files import File
from django.core.files.storage import Storage

from ..models import KasaDakaUser, CallSession, CallSessionStep
from ..models import VoiceService, Choice, ChoiceOption
from ..models import Language, VoiceLabel, VoiceFragment

def create_sample_voice_service(cls):
        cls.voice_label = VoiceLabel.objects.create(
                name = "test voicelabel")

        cls.language = Language.objects.create(
                name="Nederlands",
                code="nl",
                voice_label =  cls.voice_label,
                error_message = cls.voice_label)
        cls.language2 = Language.objects.create(
                name="English",
                code="en",
                voice_label =  cls.voice_label,
                error_message = cls.voice_label)


        cls.voice_service = VoiceService.objects.create(
                name="testservice",
                description="bla",
                active = True,
                requires_registration= True)
        cls.voice_service.supported_languages.add(cls.language)

        cls.audio_file = mock.MagicMock(spec=File, name='audio')
        cls.audio_file.name = 'audio.wav'

        # Mock storage to emulate having a file in the FileField
        cls.storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
        cls.storage_mock.url = mock.MagicMock(name='url')
        cls.storage_mock.url.return_value = '/static/audio.wav'

        with mock.patch('django.core.files.storage.default_storage._wrapped', cls.storage_mock):
            cls.voice_fragment = VoiceFragment.objects.create(
                    parent = cls.voice_label,
                    language = cls.language,
                    audio = cls.audio_file)

        cls.user = KasaDakaUser.objects.create(caller_id = cls.caller_id,
                language = cls.language,
                service = cls.voice_service)
        
        cls.session = CallSession.objects.create(service = cls.voice_service,
                user = cls.user)

        cls.choice_element = Choice.objects.create(name="keus1",
                description = "wauw wat een moeilijke keuze",
                voice_label = cls.voice_label,
                service = cls.voice_service)
        cls.voice_service._start_element = cls.choice_element
        cls.voice_service.save()

        cls.choice_option1 = ChoiceOption.objects.create(name="option1",
                description="option1 is awesome",
                parent = cls.choice_element,
                voice_label = cls.voice_label,
                _redirect = cls.choice_element,
                service = cls.voice_service)
        cls.choice_option2 = ChoiceOption.objects.create(name="option2",
                description="option2 is awesome",
                parent = cls.choice_element,
                voice_label = cls.voice_label,
                _redirect = cls.choice_element,
                service = cls.voice_service)
        
        cls.choice_url = reverse('service-development:choice' ,
                kwargs = {'session_id':cls.session.id,
                    'element_id':cls.choice_element.id})



