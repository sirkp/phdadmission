from django.contrib import admin
from django.shortcuts import get_object_or_404
from accounts.models import User
from faculty.models import ApplicantScoreByFaculty
from django.utils.translation import ugettext_lazy as _
# Register your models here.

class CustomFacultyListFilter(admin.SimpleListFilter):
    title = _('Faculty')

    parameter_name = 'faculty'

    def lookups(self, request, model_admin):
        users = User.objects.filter(is_staff=True, is_superuser=False)
        print(users)
        n = User.objects.filter(is_staff=True, is_superuser=False).count()
        facultys = []
        for i in range(n):
            item = (users[i].email,_(users[i].first_name+' '+users[i].last_name))
            facultys.append(item)
        print(facultys)
        return facultys

    def queryset(self, request, queryset):
        if(self.value()!=None):
            return queryset.filter(faculty=get_object_or_404(User, email=self.value()))

class ApplicantScoreByFacultyAdmin(admin.ModelAdmin):
    list_filter = ('willing_to_guide',CustomFacultyListFilter)
    list_display = ['faculty','application_no','willing_to_guide','assesment_score']

admin.site.register(ApplicantScoreByFaculty,ApplicantScoreByFacultyAdmin)
