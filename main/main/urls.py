from allauth.account.views import confirm_email
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_auth.registration.views import VerifyEmailView
from django.views.generic import TemplateView
from accounts.views import CustomRegisterView
# from accounts.views import CustomPasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/classe/', include('classi.urls')),
    path('api/chatmessages/', include('chatmessages.urls')),
    # lasciare in questo ordine
    # re_path(r'^rest-auth/password/reset/$', CustomPasswordResetView.as_view(),name='rest_password_reset'),
    re_path(r'^rest-auth/registration/$', CustomRegisterView.as_view(), name='rest_register'),
    re_path(r"^rest-auth/registration/confirm-email/$", VerifyEmailView.as_view(), name="account_email_verification_sent"),
    re_path(r"^rest-auth/registration/confirm-email/(?P<key>[-:\w]+)/$", confirm_email, name="account_confirm_email"),
    # re_path(r'^accounts/registration-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/profile/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
