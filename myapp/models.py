from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=30, blank=True, null=True) 
    Password =models.CharField(max_length=30,blank=True, null=True)
    Type =models.CharField(max_length=30,blank=True,null=True)

class UserTable(models.Model):
    Firstname =models.CharField(max_length=30,blank=True,null=True)
    Lastname =models.CharField(max_length=30,blank=True,null=True)
    Age =models.IntegerField(blank=True,null=True)
    Gender =models.CharField(max_length=30,blank=True,null=True)
    Place =models.CharField(max_length=30,blank=True,null=True)
    Post =models.CharField(max_length=30,blank=True,null=True)
    Pin =models.IntegerField(blank=True,null=True)
    Phone =models.BigIntegerField(blank=True,null=True)
    Email =models.CharField(max_length=30,blank=True,null=True)
    LOGIN =models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)

class StaffTable(models.Model):
    Firstname =models.CharField(max_length=30,blank=True,null=True)
    Lastname =models.CharField(max_length=30,blank=True,null=True)
    Age =models.IntegerField(blank=True,null=True)
    Gender =models.CharField(max_length=10,blank=True,null=True)
    Place =models.CharField(max_length=30,blank=True,null=True)
    Post =models.CharField(max_length=30,blank=True,null=True)
    pin =models.IntegerField(blank=True,null=True)
    Phone =models.BigIntegerField(blank=True,null=True)
    Email =models.CharField(max_length=30,blank=True,null=True)
    LOGIN =models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)

class FeedbackTable(models.Model):
    USER =models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    Feedback =models.CharField(max_length=30,blank=True,null=True)
    Date =models.DateField(blank=True,null=True)
    Rating =models.IntegerField(blank=True,null=True)

class NotificationTable(models.Model):
    Notification =models.CharField(max_length=300,blank=True,null=True)
    Date =models.DateTimeField(blank=True,null=True)

class WorkTable(models.Model):
    STAFF =models.ForeignKey(StaffTable,on_delete=models.CASCADE,blank=True,null=True)
    work =models.CharField(max_length=100,blank=True,null=True)
    Workdescription =models.CharField(max_length=300,blank=True,null=True)
    Status =models.CharField(max_length=300,blank=True,null=True)
    Assigndate =models.DateTimeField(blank=True,null=True)
    Deadline =models.DateTimeField(blank=True,null=True)

class ComplaintTable(models.Model):
    USER =models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    Complaint=models.CharField(max_length=300,blank=True,null=True)
    Date =models.DateTimeField(blank=True,null=True)
    Reply =models.CharField(max_length=300,blank=True,null=True)




