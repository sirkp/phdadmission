from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from faculty import views
from django.urls import path
from django.shortcuts import reverse

app_name='faculty'

urlpatterns = [
    path('',views.HomePage.as_view(), name='faculty_home'),
    path('login/',views.FacultyCustomLoginView.as_view(),name = 'faculty_login'),
    path('signup/', views.SignUp.as_view(), name='faculty_signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='faculty:faculty_login'),name = 'faculty_logout'),
]
