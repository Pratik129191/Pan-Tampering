from django import forms
from django.template import loader
from django.contrib.auth import authenticate
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import UserModel, \
    UserCreationForm as BaseUserCreationForm,\
    AuthenticationForm as BaseAuthenticationForm, \
    PasswordResetForm as BasePasswordResetForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from . import models


class UserCreationForm(BaseUserCreationForm):
    def save(self, commit=True):
        self.instance = models.User.objects.create_user(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password2'],
            email=self.cleaned_data['email'],
        )
        return self.instance

    class Meta(BaseUserCreationForm.Meta):
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class AuthenticationForm(BaseAuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    
# class PasswordResetForm(BasePasswordResetForm):
#     # def send_mail(
#     #         self,
#     #         subject_template_name,
#     #         email_template_name,
#     #         context,
#     #         from_email,
#     #         to_email,
#     #         html_email_template_name=None,
#     # ):
#     #     """
#     #     Send a django.core.mail.EmailMultiAlternatives to `to_email`.
#     #     """
#     #     subject = loader.render_to_string(subject_template_name, context)
#     #     # Email subject *must not* contain newlines
#     #     subject = "".join(subject.splitlines())
#     #     body = loader.render_to_string(email_template_name, context)
#     #
#     #     email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
#     #     if html_email_template_name is not None:
#     #         html_email = loader.render_to_string(html_email_template_name, context)
#     #         email_message.attach_alternative(html_email, "text/html")
#     #
#     #     email_message.send()
#
#     def save(
#             self,
#             domain_override=None,
#             subject_template_name="registration/password_reset_subject.txt",
#             email_template_name="registration/password_reset_email.html",
#             use_https=False,
#             token_generator=default_token_generator,
#             from_email=None,
#             request=None,
#             html_email_template_name=None,
#             extra_email_context=None,
#     ):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         # email = self.cleaned_data["email"]
#         email = request.POST.get('email')
#         if not domain_override:
#             current_site = get_current_site(request)
#             site_name = current_site.name
#             domain = current_site.domain
#         else:
#             site_name = domain = domain_override
#         email_field_name = UserModel.get_email_field_name()
#         for user in self.get_users(email):
#             user_email = getattr(user, email_field_name)
#             context = {
#                 "email": user_email,
#                 "domain": domain,
#                 "site_name": site_name,
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "user": user,
#                 "token": token_generator.make_token(user),
#                 "protocol": "https" if use_https else "http",
#                 **(extra_email_context or {}),
#             }
#             print(f"{domain}://{site_name}/{urlsafe_base64_encode(force_bytes(user.pk))}/{token_generator.make_token(user)}")
#             self.send_mail(
#                 subject_template_name,
#                 email_template_name,
#                 context,
#                 from_email,
#                 user_email,
#                 html_email_template_name=html_email_template_name,
#             )

