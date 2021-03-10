from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.utils.http import urlsafe_base64_decode
from django.views.generic.base import TemplateView
from django.contrib.auth.tokens import default_token_generator
#
from .models import User


class acc_active_email (View):

    def get (self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(self.kwargs.get('uid')).decode()
            user = get_object_or_404(User, pk=uid)
        except(TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, self.kwargs.get('token')):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')



class testview (TemplateView):
    template_name = 'accounts/test.html'
