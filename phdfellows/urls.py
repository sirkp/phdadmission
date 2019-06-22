from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from phdfellows import views
from django.urls import path



app_name='phdfellows'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='phdfellows_home'),
    url(r'application/$',views.ApplicationCreateView.as_view(),name = 'application'),
    url(r'application_update/(?P<pk>\d+)/$',views.ApplicationUpdateView.as_view(),name = 'update'),
    url(r'application_detail/(?P<pk>\d+)/$',views.ApplicationDetailView.as_view(),name = 'application_detail'),
]
