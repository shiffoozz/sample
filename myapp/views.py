from django.shortcuts import render
from django.views import View


#///////////////////////////admin////////////////////////////////////////////////
class Addstaff(View):
    def get(self,request):
        return render(request,"administrator/addstaff.html")
    

class Assignstaff(View):
    def get(self,request):
        return render(request,"administrator/assign.html")
    
class Complaint(View):
    def get(self,request):
        return render(request,"administrator/complaint.html")
    
class Editstaff(View):
    def get(self,request):
        return render(request,"administrator/editstaff.html")    
    
class Login(View):
    def get(self,request):
        return render(request,"administrator/login.html")    
    
class Sendnotification(View):
    def get(self,request):
        return render(request,"administrator/sendnotification.html")  

class View_staff(View):
    def get(self,request):
        return render(request,"administrator/view_staff.html")      
    
class View_user(View):
    def get(self,request):
        return render(request,"administrator/view_user.html")      
    
class Viewfeedback(View):
    def get(self,request):
        return render(request,"administrator/viewfeedback.html") 
    

#//////////////////////staff/////////////////////////////
class Feedback(View):
    def get(self,request):
        return render(request,"staff/feedback.html") 
    
class Login(View):
    def get(self,request):
        return render(request,"staff/login.html") 
    
class Notification(View):
    def get(self,request):
        return render(request,"staff/notification.html") 

class Update(View):
    def get(self,request):
        return render(request,"staff/update.html") 

class Updatestatus(View):
    def get(self,request):
        return render(request,"staff/updatestatus.html") 

class Viewservice(View):
    def get(self,request):
        return render(request,"staff/viewservice.html") 