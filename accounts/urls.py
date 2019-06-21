from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views
from django.urls import path



app_name='accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'logout/$',auth_views.LogoutView.as_view(next_page='home'),name = 'logout'),
]
