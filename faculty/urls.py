from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from faculty import views
from django.urls import path
from django.shortcuts import reverse

app_name='faculty'

urlpatterns = [
    path('',views.HomePage.as_view(), name='faculty_home'),
    url(r'student_application_update/(?P<pk>\d+)/$',views.StudentApplicationUpdateView.as_view(),name = 'student_application_update'),
]
