from django.shortcuts import render, reverse, redirect, get_object_or_404
from accounts.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from dropdown.models import PGDiscipline, UGDiscipline, BranchQualifyingExamination
from phdfellows.models import Application, WrittenTestScore
from faculty.models import ApplicantScoreByFaculty
from faculty.forms import StudentApplicationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView,TemplateView, RedirectView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from braces import views

# Create your views here.
class NotLockedRequiredMixin:
    """
    Checks if user is locked
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_locked:
            raise PermissionDenied
            return redirect('home')
        return super(NotLockedRequiredMixin, self).dispatch(request,
            *args, **kwargs)


class StudentApplicationUpdateView(views.LoginRequiredMixin,views.StaffuserRequiredMixin,NotLockedRequiredMixin, UpdateView):#Always put mixins on left
    """
    View to show faculty Student details, assesment score(if given test) and  update their status.
    This view is linked with phdadmission/faculty/templates/faculty/student_application_update.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = Application
    form_class = StudentApplicationForm
    context_object_name = 'application'
    success_url = reverse_lazy('faculty:faculty_home')
    template_name = 'faculty/student_application_update.html'

    def form_valid(self,form):
        if(self.request.POST['current_status']=='Shortlisted for Test'):
            written_test_score = WrittenTestScore(application_no=get_object_or_404(Application,pk=self.object.pk))
            written_test_score.save()

        self.object = form.save(commit=False)
        if(self.request.POST['current_status']=='Shortlisted for Interview'):
            self.object.was_selected_for_interview = True

        if(self.object.was_selected_for_interview and (self.request.POST['current_status']=='Selected' or self.request.POST['current_status']=='Rejected')):
            faculty_assessment = ApplicantScoreByFaculty(faculty=self.request.user,application_no=get_object_or_404(Application,pk=self.object.pk),willing_to_guide=self.request.POST['willing_to_guide'],assesment_score=self.request.POST['assesment_score'],remarks=self.request.POST['remarks'])
            faculty_assessment.save()
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = get_object_or_404(Application,pk=self.object.pk)
        if(application.current_status == 'Shortlisted for Interview' or application.current_status == 'Shortlisted for Test'):
            written_test_score = get_object_or_404(WrittenTestScore,application_no=application)
            context["written_test_score"] = written_test_score
        return context

class HomePage(views.LoginRequiredMixin,views.StaffuserRequiredMixin,NotLockedRequiredMixin,ListView):
    """
    view to search applications.
    This view is linked with phdadmission/faculty/templates/faculty/faculty_home.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    template_name = 'faculty/faculty_home.html'
    context_object_name = 'results'

    name = ''
    air = ''
    scale_of_score_ug = ''
    score_ug = ''
    scale_of_score_pg = ''
    score_pg = ''
    ug_branch = ''
    pg_branch = ''
    gate_or_net_branch = ''
    current_status = ''
    year = ''

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

        ug_disciplines = UGDiscipline.objects.all()
        ug_disciplines = ug_disciplines.order_by('ug_discipline')
        context['ug_disciplines'] = ug_disciplines

        branch_qualifying_exam = BranchQualifyingExamination.objects.all()
        branch_qualifying_exam = branch_qualifying_exam.order_by('branch')
        context['branch_qualifying_exam'] = branch_qualifying_exam

        pg_disciplines = PGDiscipline.objects.all()
        pg_disciplines = pg_disciplines.order_by('pg_discipline')
        context['pg_disciplines'] = pg_disciplines

        return context

    def get_queryset(self):##all, result, no result
        #getting fields
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
            self.current_status=''

        if(self.year == None):
            self.year=''

        # query
        applications = Application.objects.all()

        applications = applications.filter(~Q(current_status='Draft'))

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

        if(self.year != ''):
            current_year = int(year,10)
            applications = applications.filter(submitted_at__year=current_year)

        if(self.current_status!=''):
            applications = applications.filter(current_status=self.current_status)
        return applications
