from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.db.models import Q
from phdfellows.models import Application
from faculty.forms import LoginForm, SignupForm
from faculty.models import Faculty, Email
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView,TemplateView, RedirectView, ListView
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
    model = Faculty
    template_name = 'registration/login.html'

    def get_redirect_url(self):
        return reverse('faculty:faculty_home')

class HomePage(LoginRequiredMixin,ListView):
    name = ''
    air = ''
    scale_of_score_ug = ''
    score_ug = ''
    scale_of_score_pg = ''
    score_pg = ''
    ug_branch = ''
    pg_branch = ''
    gate_or_net_branch = ''
    current_status = 'Submitted'
    year = ''
    login_url = 'faculty:faculty_login'
    template_name = 'faculty/faculty_home.html'
    context_object_name = 'results'

    # def get(self, request):
    #     self.name = self.request.GET.get('name')
    #     self.air = self.request.GET.get('air')
    #     print(self.request.GET.get('name'))
    #     print(self.request.GET.get('air'))
    #     if(self.name == None):
    #         self.name=''
    #     if(self.air == None):
    #         self.air=''
    #     return render(request, 'faculty/faculty_home.html', {'name':self.name, 'air':self.air})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.name
        context["air"] = self.air
        context["scale_of_score_ug"] = self.scale_of_score_ug
        context["score_ug"] = self.score_ug
        context["scale_of_score_pg"] = self.scale_of_score_pg
        context["score_pg"] = self.score_pg
        context["ug_branch"] = self.ug_branch
        context["pg_branch"] = self.pg_branch
        context["gate_or_net_branch"] = self.gate_or_net_branch
        context["current_status"] = self.current_status
        context["year"] = self.year
        return context

    def get_queryset(self):##all, result, no result
        self.name = self.request.GET.get('name')

        self.air = self.request.GET.get('air')

        self.scale_of_score_ug = self.request.GET.get('scale_of_score_ug')
        self.score_ug = self.request.GET.get('score_ug')

        self.scale_of_score_pg = self.request.GET.get('scale_of_score_pg')
        self.score_pg = self.request.GET.get('score_pg')

        self.ug_branch = self.request.GET.get('ug_branch')

        self.pg_branch = self.request.GET.get('pg_branch')

        self.gate_or_net_branch = self.request.GET.get('gate_or_net_branch')

        self.current_status = self.request.GET.get('current_status')

        self.year = self.request.GET.get('year')


        print(self.name)
        print(self.air)
        print(self.scale_of_score_ug)
        print(self.score_ug)
        print(self.scale_of_score_pg)
        print(self.score_pg)
        print(self.ug_branch)
        print(self.pg_branch)
        print(self.gate_or_net_branch)
        print(self.current_status)
        print(self.year)


        if(self.name == None):
            self.name=''

        if(self.air == None):
            self.air=''

        if(self.scale_of_score_ug == None):
            self.scale_of_score_ug=''

        if(self.score_ug == None):
            self.score_ug=''

        if(self.scale_of_score_pg == None):
            self.scale_of_score_pg=''

        if(self.score_pg == None):
            self.score_pg=''

        if(self.ug_branch == None):
            self.ug_branch=''

        if(self.pg_branch == None):
            self.pg_branch=''

        if(self.gate_or_net_branch == None):
            self.gate_or_net_branch=''

        if(self.current_status == None):
            self.current_status='Submitted'

        if(self.year == None):
            self.year=''

        # query
        applications = Application.objects.all()

        applications = applications.filter(current_status=self.current_status)

        if(self.name != ''):
            if(' ' in self.name):
                first_name = self.name.split(' ')[0]
                last_name = self.name.split(' ')[1]
                applications = applications.filter(first_name__iexact=first_name, last_name__iexact=last_name)
            else:
                applications = applications.filter(Q(first_name__startswith=self.name) | Q(last_name__icontains=self.name))

        if(self.air != ''):# [ )
            if('-' in self.air):
                lb = self.air.split('-')[0]
                ub = self.air.split('-')[1]
                lower_bound = int(lb,10)
                upper_bound = int(ub,10)
                applications = applications.filter(all_india_rank_in_qualifying_exam__gte=lower_bound, all_india_rank_in_qualifying_exam__lt=upper_bound)
            else:
                lb = self.air.split('+')[0]
                lower_bound = int(lb,10)
                applications = applications.filter(all_india_rank_in_qualifying_exam__gte=lower_bound)

        if(self.scale_of_score_ug != ''):
            applications = applications.filter(scale_of_score_ug=self.scale_of_score_ug)

        if(self.score_ug != ''):# ( ]
            lb = self.score_ug.split('-')[0]
            ub = self.score_ug.split('-')[1]
            lower_bound = float(lb)
            upper_bound = float(ub)
            applications = applications.filter(score_in_ug__gt=lower_bound, score_in_ug__lte=upper_bound)

        if(self.scale_of_score_ug != ''):
            applications = applications.filter(scale_of_score_ug=self.scale_of_score_ug)

        if(self.score_ug != ''):# ( ]
            lb = self.score_ug.split('-')[0]
            ub = self.score_ug.split('-')[1]
            lower_bound = float(lb)
            upper_bound = float(ub)
            applications = applications.filter(score_in_ug__gt=lower_bound, score_in_ug__lte=upper_bound)

        if(self.ug_branch!=''):
            applications = applications.filter(ug_discipline=self.ug_branch)

        #####
        if(self.score_pg != ''):# ( ]
            lb = self.score_pg.split('-')[0]
            ub = self.score_pg.split('-')[1]
            lower_bound = float(lb)
            upper_bound = float(ub)
            applications = applications.filter(score_in_pg__gt=lower_bound, score_in_pg__lte=upper_bound)

        if(self.scale_of_score_pg != ''):
            applications = applications.filter(scale_of_score_pg=self.scale_of_score_pg)

        if(self.score_pg != ''):# ( ]
            lb = self.score_pg.split('-')[0]
            ub = self.score_pg.split('-')[1]
            lower_bound = float(lb)
            upper_bound = float(ub)
            applications = applications.filter(score_in_pg__gt=lower_bound, score_in_pg__lte=upper_bound)

        if(self.pg_branch!=''):
            applications = applications.filter(pg_discipline=self.pg_branch)

        if(self.gate_or_net_branch!=''):
            applications = applications.filter(branch_code_for_qualifying_exam=self.gate_or_net_branch)

        # if(self.current_status != ''):
        #     applications = applications.filter(current_status=self.current_status)

        if(self.year != ''):
            current_year = int(year,10)
            applications = applications.filter(submitted_at__year=current_year)
        return applications
        ###
        # if (self.name !=''):
        #     first_name = self.name.split(' ')[0]
        #     last_name = self.name.split(' ')[1]
        #     print(Application.objects.filter(first_name=first_name, last_name=last_name))
        #     return Application.objects.filter(first_name=first_name, last_name=last_name)
