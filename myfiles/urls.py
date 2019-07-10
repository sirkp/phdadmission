from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from myfiles import views
from django.urls import path



app_name='upload'

urlpatterns = [
    path('',views.UploadAnnouncementsView.as_view(), name= 'upload_announcements'),
    path('announcements_list/',views.AnnouncementsListView.as_view(), name = 'announcements_list'),
    path('delete_announcement/<int:pk>/', views.AnnouncementsDeleteView.as_view(), name='delete_announcement'),
]
