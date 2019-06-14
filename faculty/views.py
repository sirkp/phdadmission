from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from faculty.forms import LoginForm, SignupForm
from faculty.models import Faculty, Email
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView,TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('faculty:faculty_login')
    template_name = 'faculty/faculty_signup.html'

    def form_valid( self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.email
        self.object.save()
        return super().form_valid(form)

class FacultyCustomLoginView(LoginView, RedirectView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_redirect_url(self):
        return reverse('faculty:faculty_home')

class HomePage(LoginRequiredMixin,TemplateView):
    login_url = 'faculty:faculty_login'
    template_name = 'faculty/faculty_home.html'
