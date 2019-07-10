from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from myfiles.models import Announcements
from myfiles.forms import AnnouncementsForm
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from braces import views
# Create your views here.
class UploadAnnouncementsView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, CreateView):
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    form_class = AnnouncementsForm
    success_url = reverse_lazy('upload:announcements_list')
    template_name = 'myfiles/upload_announcements.html'

class AnnouncementsListView(views.LoginRequiredMixin, views.SuperuserRequiredMixin,ListView):
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = Announcements
    template_name = 'myfiles/announcements_list.html'
    context_object_name = 'announcements'

class AnnouncementsDeleteView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, DeleteView):
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = Announcements
    success_url = reverse_lazy('upload:announcements_list')
