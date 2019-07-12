from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from myfiles import views
from django.urls import path



app_name='upload'

urlpatterns = [
    path('announcements/',views.UploadAnnouncementsView.as_view(), name= 'upload_announcements'),
    path('omr_sheets/',views.UploadOMRSheetsView.as_view(), name= 'upload_omr_sheets'),
    path('announcements_list/',views.AnnouncementsListView.as_view(), name = 'announcements_list'),
    path('omr_sheets_list/',views.OMRSheetsListView.as_view(), name = 'omr_sheets_list'),
    path('delete_announcement/<int:pk>/', views.AnnouncementsDeleteView.as_view(), name='delete_announcement'),
    path('delete_omr_sheet/<int:pk>/', views.OMRSheetDeleteView.as_view(), name='delete_omr_sheet'),
]
