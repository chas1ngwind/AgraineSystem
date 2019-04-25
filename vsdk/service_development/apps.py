from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ServiceDevelopmentConfig(AppConfig):
    name = 'vsdk.service_development'
    verbose_name = _("Voice Service Development")
