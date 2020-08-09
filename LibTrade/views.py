from django.contrib.auth import login, logout
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.views.generic import (CreateView, TemplateView,DetailView, UpdateView, ListView, FormView)
from django.views import View
from django.contrib.auth import get_user_model
from accounts.models import User
from LibTrade.forms import SignUpForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.urls import reverse

import smtplib

# from validate_email import validate_email

from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
# from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .utils import account_activation_token




import smtplib
hostt = "smtp.gmail.com"
portt = 587
usernamee = "libtrad345@gmail.com"
passwordd = "@@sai@@@"


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'LibTrade/user_detail.html'

class Landing(TemplateView):
    template_name = 'LibTrade/landing.html'
class EmailExistsView(TemplateView):
    template_name = 'LibTrade/emailexists.html'

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'Libtrade/signup.html'

    def get_context_data(self, **kwargs):
        # kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        userobj = User.objects.filter(email = user.email)
        to_email = user.email
        if len(userobj)!=0:
            return redirect('emailexists')

        user.slug = slugify(user.username)
        user.is_active = False

        user.save()
        subject="Thank UUUUUU"
        message="watooott"
        email_conn = smtplib.SMTP(hostt, portt)
        email_conn.starttls()
        email_conn.login(usernamee, passwordd)
        current_site = get_current_site(self.request)
        email_body = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
        }
        link = reverse('activate', kwargs={'uidb64': email_body['uid'], 'token': email_body['token']})
        email_subject = 'Activate your account'
        activate_url = 'http://'+current_site.domain+link
        email_bod = 'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url+" "+str(user.pk)
        email_conn.sendmail(usernamee, [self.request.POST['email'],usernamee], email_bod)

        login(self.request, user)
        return redirect('home')


class VerificationView(View):

    def get(self, request, uidb64, token):
        id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=id)

        if user.is_active:
            return redirect('accounts:booklist')

        user.is_active = True
        user.save()
        return redirect('accounts:booklist')

        return redirect('signup')



        # if not account_activation_token.check_token(user, token):
        #     return redirect('login'+'?message='+'User already activated')

class LoginView(LoginView):
    template_name = 'LibTrade/login.html'
    success_url = reverse_lazy('LibTrade/home.html')
    redirect_authenticated_user =- True


@method_decorator([login_required], name='dispatch')
class Home(TemplateView):
    template_name = 'Libtrade/user_detail.html'
    model = User
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        return context
