from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views
from django.urls import path



app_name='accounts'

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), {'template_name': "registration/password_reset_form.html"}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView,{'template_name': "registration/password_reset_done.html"},name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView,{'template_name': "registration/password_reset_confirm.html"},name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView,{'template_name': "registration/password_reset_complete.html"},name='password_reset_complete'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'logout/$',auth_views.LogoutView.as_view(next_page='home'),name = 'logout'),
]
