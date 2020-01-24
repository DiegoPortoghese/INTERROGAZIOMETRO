from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Override della DefaultAccountAdapter di allauth
    per personalizzare l'url della conferma registrazione
    """
    def get_email_confirmation_url(self, request, emailconfirmation):
        return '{0}/account/registration-confirm/?key={1}'.format(
            settings.FRONTEND_PROTOCOL + '://' + settings.FRONTEND_DOMAIN,
            emailconfirmation.key)