from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import KasaDakaUser, CallSession, Language

from . import base

class KasaDakaUserRegistration(TemplateView):

    def create_new_user(self, request, session):
        """
        After all required elements of the registration process
        have been filled, this function creates the user.
        After registration the user is redirected back to the start
        of the voice service.
        """
        caller_id = session.caller_id
        #register the user and link the session to the user
        user = KasaDakaUser(caller_id = caller_id,
                service = session.service)
        if session.service.registration_language:
            user.language = session.language
        #if session.service.registration_name:
        #    pass

        user.save()
        session.link_to_user(user)

        session.record_step(None, "Registered as user: %s" % str(user))
        return

    def user_registration_process(self, request, session):
        """
        This function redirects to the set elements of the user registration
        process, and redirects to the final registration when all elements have
        been filled.
        """
        # Always redirect back to registration process
        redirect_url = reverse('service-development:user-registration', args =[session.id])
        if session.service.registration_language and session.language == None:
            return base.redirect_add_get_parameters('service-development:language-selection', session.id,
                    redirect_url = redirect_url)
        
        #TODO: dit verder uitwerken, user bestaat natuurlijk nog niet dus daar kun je niet checken. 
        #if 'name' in session.service.registration_elements and session.user.name_voice == None:
            # go to user name voice prompt
        #    pass

        # If all required elements are present, finalize registration by creating a new user
        self.create_new_user(request, session)

        # Return to start of voice service
        return redirect('service-development:voice-service', voice_service_id = session.service.id, session_id = session.id)

    def get(self, request, session_id):
        session = get_object_or_404(CallSession, pk = session_id)
        return self.user_registration_process(request, session)
