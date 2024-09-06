
from django.contrib import admin
from django.urls import path
from attendance.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('admin_home',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('logout',logout,name='logout'),
    path('mark_attendance',mark_attendance,name='mark_attendance'),
    path('view_attendance',view_attendance,name='view_attendance'),
    path('searchday',searchday,name='searchday'),
    path('view_students',view_students,name='view_students'),
    path('student/<int:id>',student,name='student'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('feedback',feedback,name='feedback'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('view_feedback',view_feedback,name='view_feedback'),
    path('delete_feedback/<int:id>',delete_feedback,name='delete_feedback'),
    path('all_attendance',all_attendance,name='all_attendance'),
    path('present_user/<int:id>',present_user,name='present_user'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
