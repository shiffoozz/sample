


from django.contrib import admin
from django.urls import  path

from myapp.views import Addstaff, Assignstaff, Complaint, Editstaff, Feedback, Login, Notification, Sendnotification, Update, Updatestatus, View_staff, View_user, Viewfeedback, Viewservice

urlpatterns = [
#/////////////////admin//////////////////////////////
    path('Addstaff',Addstaff.as_view(),name='Addstaff'),
    path('Assignstaff',Assignstaff.as_view(),name='Assignstaff'),
    path('Complaint',Complaint.as_view(),name='Complaint'),
    path('Editstaff',Editstaff.as_view(),name='Editstaff'),
    path('Login',Login.as_view(),name='Login'),
    path('Sendnotification',Sendnotification.as_view(),name='Sendnotification'),
    path('View_staff',View_staff.as_view(),name='View_staff'),
    path('View_user',View_user.as_view(),name='View_user'),
    path('Viewfeedback',Viewfeedback.as_view(),name='Viewfeedback'),

#//////////////////////staff//////////////////////////
    
    path('Feedback',Feedback.as_view(),name='Feedback'),
    path('Login',Login.as_view(),name='Login'),
    path('Notification',Notification.as_view(),name='Notification'),
    path('Update',Update.as_view(),name='Update'),
    path('Updatestatus',Updatestatus.as_view(),name='Updatestatus'),
    path('Viewservice',Viewservice.as_view(),name='Viewservice'),

    

    

    

    

    



    
    

    ]
