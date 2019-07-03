from django.http import HttpResponse
import datetime
from django.utils.timezone import make_aware
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from phdfellows.forms import ApplicationForm
from phdfellows import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from phdfellows.models import Application
from accounts.models import User
from dropdown.models import (Category, BranchQualifyingExamination, Country,
                                    PGDiscipline, ResearchArea, State, TypeOfWork,
                                     UGDiscipline)
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import (RedirectView, View, TemplateView,
                                    ListView, DetailView, CreateView, UpdateView,
                                    DeleteView)
UserModel = get_user_model()



class HomePage(LoginRequiredMixin,ListView):
    login_url = 'home'
    model = User
    template_name = 'phdfellows/homepage.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(email=self.request.user.email)

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    login_url = 'home'
    form_class = ApplicationForm
    success_url = reverse_lazy('phdfellows:phdfellows_home')
    template_name = 'phdfellows/application.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.first_name = self.request.user.first_name
        self.object.last_name = self.request.user.last_name
##########
        if(self.object.category == 'Other'):
            self.object.is_category_other = True
            self.object.category = self.request.POST.get('category_other')
###########
        if (self.object.country != '' and self.object.country!='India'):
            self.object.state = self.request.POST.get('state_description')
        self.object.email = self.request.user.email
        self.object.save()

        if('submit_application' in self.request.POST):
            self.object = form.save(commit=False)
            my_time=datetime.datetime.now()
            my_time=make_aware(my_time)
            n=Application.objects.filter(submitted_at__year=my_time.year).count() + 1
            app_no = ((my_time.year % 100) * 100000) + n
            self.object.submitted_at = datetime.date.today()
            self.object.submitted_year = my_time.year
            self.object.application_no = app_no
            self.object.previous_status = self.object.current_status
            self.object.current_status = "Submitted"
            self.object.save()
        return super().form_valid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categorys = Category.objects.all()
        categorys = categorys.order_by('category')
        context['categorys'] = categorys

        countrys = Country.objects.all()
        context['countrys'] = countrys

        branch_qualifying_exam = BranchQualifyingExamination.objects.all()
        branch_qualifying_exam = branch_qualifying_exam.order_by('branch')
        context['branch_qualifying_exam'] = branch_qualifying_exam

        states = State.objects.all()
        states = states.order_by('state')
        context['states'] = states

        research_areas = ResearchArea.objects.all()
        research_areas = research_areas.order_by('research_area')
        context['research_areas'] = research_areas

        type_of_works = TypeOfWork.objects.all()
        type_of_works = type_of_works.order_by('type_of_work')
        context['type_of_works'] = type_of_works

        ug_disciplines = UGDiscipline.objects.all()
        ug_disciplines = ug_disciplines.order_by('ug_discipline')
        context['ug_disciplines'] = ug_disciplines

        pg_disciplines = PGDiscipline.objects.all()
        pg_disciplines = pg_disciplines.order_by('pg_discipline')
        context['pg_disciplines'] = pg_disciplines

        return context

class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'home'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('phdfellows:phdfellows_home')
    template_name = 'phdfellows/application_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if (self.object.country != '' and self.object.country!='India'):
            self.object.state = self.request.POST.get('state_description')
            self.object.save()

        if('submit_application' in self.request.POST):
            self.object = form.save(commit=False)
            my_time=datetime.datetime.now()
            my_time=make_aware(my_time)
            n=Application.objects.filter(submitted_at__year=my_time.year).count() + 1
            app_no = ((my_time.year % 100) * 100000) + n
            self.object.submitted_at = datetime.date.today()
            self.object.submitted_year = my_time.year
            self.object.application_no = app_no
            self.object.previous_status = self.object.current_status
            self.object.current_status = "Submitted"
            self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categorys = Category.objects.all()
        context['categorys'] = categorys

        country = Country.objects.all()
        context['country'] = country

        branch_qualifying_exam = BranchQualifyingExamination.objects.all()
        context['branch_qualifying_exam'] = branch_qualifying_exam

        state = State.objects.all()
        context['state'] = state

        research_area = ResearchArea.objects.all()
        context['research_area'] = research_area

        type_of_work = TypeOfWork.objects.all()
        context['type_of_work'] = type_of_work

        ug_discipline = UGDiscipline.objects.all()
        context['ug_discipline'] = ug_discipline

        pg_discipline = PGDiscipline.objects.all()
        context['pg_discipline'] = pg_discipline

        return context

class ApplicationDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'application_detail'
    model = Application
    template_name = 'phdfellows/application_detail.html'
