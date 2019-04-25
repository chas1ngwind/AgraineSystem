from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from ..models import VoiceService, lookup_or_create_session, lookup_kasadaka_user_by_caller_id

from . import base

def get_caller_id_from_GET_request(request):
    if 'caller_id' in request.GET:
        return request.GET['caller_id']
    elif 'callerid' in request.GET:
        return request.GET['callerid']
    return None



def voice_service_start(request, voice_service_id, session_id = None):
    """
    Starting point for a voice service. Looks up user (redirects to registation
    otherwise), creates session, (redirects to language selection).
    If all requirements are fulfilled, redirects to the starting element of the
    voice service.
    """
    voice_service = get_object_or_404(VoiceService, pk=voice_service_id)

    #if not voice_service.active:
        # TODO give a nicer error message
        #raise Http404()

    caller_id = get_caller_id_from_GET_request(request)
    session = lookup_or_create_session(voice_service, session_id, caller_id)
    session_id = session.id

    # If the session is not yet linked to an user, try to look up the user by
    # Caller ID, and link it to the session. If the user cannot be found,
    # redirect to registration.
    if caller_id and not session.user:
        found_user = lookup_kasadaka_user_by_caller_id(caller_id, session.service)
        if found_user:
            session.link_to_user(found_user)

        # If there is no user with this caller_id and registration of users is preferred or required, redirect to registration
        elif voice_service.registration_preferred_or_required:
            return redirect('service-development:user-registration',
                    session.id)

    # If there is no caller_id provided, and user registration is required for this service,
    # throw an error
    elif voice_service.registration_required and not caller_id:
        # TODO make this into a nice audio error
        raise ValueError('This service requires registration, but registration is not possible, because there is no callerID!')



    # If the language for this session can not be determined,
    # redirect the user to language selection for this session only.
    if not session.language:
        # After selection of language, return to start of voice service.
        return_url = reverse('service-development:voice-service', args = [session.service.id,session.id])
        return base.redirect_add_get_parameters('service-development:language-selection',
                        session.id,
                        redirect_url = return_url)
    return base.redirect_to_voice_service_element(voice_service.start_element, session)
