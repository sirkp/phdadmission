from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from phdfellows.forms import SignupForm, ApplicationForm
from phdfellows import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from phdfellows.models import PhdFellows,Application
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import get_user_model
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,CreateView,UpdateView,
                                    DeleteView)
UserModel = get_user_model()

class HomePage(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = PhdFellows
    template_name = 'phdfellows/homepage.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(email=self.request.user.email)
    # def get(self, request):
    #     user = self.request.user
    #     print(user)
    #     return render(request, self.template_name)
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION!'
    #     # injectme is the key
    #     return context



def signup(request):
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
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration. To login go back to  Homepage')
    else:
        form = SignupForm()
    return render(request, 'phdfellows/signup.html', {'form': form})

def activate(request, uidb64, token):
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

# class ApplicationListView(LoginRequiredMixin, ListView):
#     login_url = '/login'
#     model = Application
#     template_name = 'phdfellows/homepage.html'
#     context_object_name = 'applications'
#
#     def get_queryset(self):
#         return Application.objects.filter(email=self.request.user.email)

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    form_class = ApplicationForm
    success_url = reverse_lazy('phdfellows:home')
    template_name = 'phdfellows/application.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.first_name = self.request.user.first_name
        self.object.last_name = self.request.user.last_name
        self.object.email = self.request.user.email
        self.object.save()
        return super().form_valid(form)

class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('phdfellows:home')
    template_name = 'phdfellows/application.html'

    def form_valid(self, form):
        if('submit_application' in self.request.POST):
            self.object = form.save(commit=False)
            self.object.previous_status = self.object.current_status
            self.object.current_status = "Submitted"
            self.object.save()
        return super().form_valid(form)

# ###############
# ###############
# class SubmitApplication(LoginRequiredMixin,View):
#     login_url = '/login'
#     form_class = ApplicationSubmitForm
#     success_url = reverse_lazy('phdfellows:home')
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.previous_status = self.object.current_status
#         self.object.current_status = "Submitted"
#         return super().form_valid(form)
# #################
# ##################
