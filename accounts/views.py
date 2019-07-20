from django.http import HttpResponse
from dateutil.relativedelta import *
from datetime import *
from myfiles.models import Announcement
from django.utils.timezone import make_aware
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from accounts.forms import SignupForm, LoginForm
from accounts import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from accounts.models import User
from django.urls import reverse_lazy
from django.utils.timezone import make_aware
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import (RedirectView, View, TemplateView,
                                    ListView, DetailView, CreateView, UpdateView,
                                    DeleteView)
from dateutil.relativedelta import relativedelta
UserModel = get_user_model()

class CustomLoginView(LoginView,RedirectView):
    """
    It determines the authenticatation process from log in, and redirects the user.
    This view is linked with phdadmission/templates/home.html
    """
    form_class = LoginForm
    template_name = 'home.html'

    def get_redirect_url(self):
        """
        It redirects to respective homepage of user
        """
        if(self.request.user.is_superuser):
            return reverse( 'admin:index' )
        elif(self.request.user.is_staff):
            return reverse( 'faculty:faculty_home' )
        else:
            return reverse('phdfellows:phdfellows_home')

    def get_context_data(self, **kwargs):
        """
        It provides data to notice board(announcements).It will provide data that six months old
        """
        context = super().get_context_data(**kwargs)

        six_months_ago = datetime.now()+relativedelta(months = -6)
        six_months_ago = make_aware(six_months_ago)
        announcements = Announcement.objects.all()
        announcements = announcements.filter(date_uploaded__gte=six_months_ago)
        context['announcements'] = announcements

        return context

def signup(request):
    """
    backend for signup, sends activation mail to user
    This view is linked with phdadmission/accounts/templates/accounts/signup.html
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_email = request.POST['email']
            user = form.save(commit=False)
            user.is_active = False
            user.username = user_email
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your IIT Ropar PhD Portal account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration. To login go back to  Homepage')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def activate(request, uidb64, token):
    """
    It makes the unique url that is to be sent in email to user for activation
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
