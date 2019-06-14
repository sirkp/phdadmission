from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from phdfellows import views
from django.urls import path



app_name='phdfellows'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'logout/$',auth_views.LogoutView.as_view(next_page='phdfellows:home'),name = 'logout'),
    url(r'application/$',views.ApplicationCreateView.as_view(),name = 'application'),
    url(r'update/(?P<pk>\d+)/$',views.ApplicationUpdateView.as_view(),name = 'update'),
    url(r'application_detail/(?P<pk>\d+)/$',views.ApplicationDetailView.as_view(),name = 'application_detail'),
]
