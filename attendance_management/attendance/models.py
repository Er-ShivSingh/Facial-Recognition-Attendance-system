from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=20,null=True)
    course = models.CharField(max_length=30,null=True)
    rno = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username

class Attendance(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    rollno = models.CharField(max_length=30,null=True)
    course = models.CharField(max_length=30,null=True)
    date = models.CharField(max_length=30,null=True)
    image = models.CharField(max_length=536170,null=True)
    status = models.CharField(max_length=30,null=True)


class Feedback(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    mobile = models.CharField(max_length=30,null=True)
    feedback = models.CharField(max_length=30,null=True)

class Record(models.Model):
    date = models.CharField(max_length=30,null=True,unique=True)
    day = models.CharField(max_length=30,null=True)

