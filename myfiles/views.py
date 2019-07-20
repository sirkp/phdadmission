from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from myfiles.models import Announcement, OMRSheet
from myfiles.forms import AnnouncementsForm, OMRSheetsForm
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from braces import views
from datetime import *
from django.utils.timezone import make_aware
from dateutil.relativedelta import relativedelta
# Create your views here.
class UploadAnnouncementsView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, CreateView):
    """
    view for uploading announcements(files or images) by admin only
    This view is linked with phdadmission/myfiles/templates/myfiles/upload_announcements.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    form_class = AnnouncementsForm
    success_url = reverse_lazy('upload:announcements_list')
    template_name = 'myfiles/upload_announcements.html'

class AnnouncementsListView(views.LoginRequiredMixin, views.SuperuserRequiredMixin,ListView):
    """
    view to display uploaded announcements
    This view is linked with phdadmission/myfiles/templates/myfiles/announcements_list.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = Announcement
    template_name = 'myfiles/announcements_list.html'
    context_object_name = 'announcements'

class AnnouncementsDeleteView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, DeleteView):
    """
    view to delete announcements
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = Announcement
    success_url = reverse_lazy('upload:announcements_list')

class UploadOMRSheetsView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, CreateView):
    """
    view for uploading omrsheet images(multiple) by admin only
    This view is linked with phdadmission/myfiles/templates/myfiles/upload_omr_sheets.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    form_class = OMRSheetsForm
    template_name = 'myfiles/upload_omr_sheets.html'

    def post(self, request):
        form = OMRSheetsForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.my_images.name, 'url': photo.my_images.url, 'url': photo.pk}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        """
        display uploaded images today
        """
        context = super().get_context_data(**kwargs)

        omr_sheets = OMRSheet.objects.all()
        one_day_ago = datetime.now()+relativedelta(days = -1)
        one_day_ago = make_aware(one_day_ago)
        omr_sheets= omr_sheets.filter(uploaded_at__gte=one_day_ago)
        context['omr_sheets'] = omr_sheets

        return context

class OMRSheetsListView(views.LoginRequiredMixin, views.SuperuserRequiredMixin,ListView):
    """
    view to display uploaded all omr sheets images
    This view is linked with phdadmission/myfiles/templates/myfiles/omr_sheets_list.html
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = OMRSheet
    template_name = 'myfiles/omr_sheets_list.html'
    context_object_name = 'omr_sheets'

class OMRSheetDeleteView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, DeleteView):
    """
    view to delete omrsheet images
    """
    redirect_unauthenticated_users = True
    raise_exception = True
    login_url = 'home'
    model = OMRSheet
    success_url = reverse_lazy('upload:omr_sheets_list')
