from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings


class CustomPasswordResetForm(PasswordResetForm):

    def save(self, domain_override=None,
             subject_template_name='account/email/password_reset_subject.txt',
             email_template_name='account/email/password_reset_email.txt',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
                
        for user in self.get_users(email):

            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override

            context = {
                'email': email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
                **(extra_email_context or {}),
            }

            # override
            context["protocol"] = settings.FRONTEND_PROTOCOL
            context["domain"] = settings.FRONTEND_DOMAIN
            context["site_name"] = settings.FRONTEND_NAME
            from_email = ''

            self.send_mail(
                subject_template_name, email_template_name, context, '',
                email, html_email_template_name=html_email_template_name,
            )
