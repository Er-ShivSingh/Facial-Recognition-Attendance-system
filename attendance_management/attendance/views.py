from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *



def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error,'error':error}
    return render(request,'login.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        cr = request.POST['course']
        rno = request.POST['rollno']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,rno=rno,course=cr,image=i,gender=gen,address=addr,dob=d)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

import datetime
current_date = datetime.datetime.now()
crdate = str(current_date.day)+"-"+str(current_date.month)+"-"+str(current_date.year)
week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
from datetime import datetime
dt = datetime.now()
x = dt.weekday()
day = week[x]
def mark_attendance(request):
    error=""
    data = User.objects.get(id=request.user.id)
    data2 = Signup.objects.get(user=request.user)
    data3 = Attendance.objects.filter(email__icontains=request.user.username)
    if request.method == 'POST':
        n = data.first_name +" "+ data.last_name
        r = data2.rno
        c = data2.course
        e = request.user.username
        img = request.POST['user-photo']
        for i in data3:
            print(i.date,crdate)
            if str(i.date)==str(crdate):
                print("hello")
                error="present"
                break
        else:
            try:
                Attendance.objects.create(name=n,email=e,rollno=r,course=c,date=crdate,image=img,status="Present")
                error="no"
            except:
                error="yes"
            try:
                Record.objects.create(date=crdate,day=day)
            except:pass
    d = {'data':data,'data2':data2,'error':error,'date':crdate}
    return render(request,'mark_attendance.html',d)

def view_attendance(request):
    data = Attendance.objects.filter(email__icontains=request.user)
    d = {'data':data}
    return render(request,'view_attendance.html',d)

def searchday(request):
    n=request.POST['name2']
    data = Attendance.objects.filter(date__icontains=n)
    d={'data':data}
    return render(request,'view_attendance.html',d)

def view_students(request):
    data = Signup.objects.all()
    data = data[::-1]
    d = {'data':data}
    return render(request,'view_students.html',d)

def student(request,id):
    data = User.objects.get(id=id)
    data2 = Signup.objects.get(user=data)
    d = {'data':data,'data2':data2}
    return render(request,'student.html',d)

def delete_user(request,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('view_students')

def feedback(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        f = request.POST['feedback']
        try:
            Feedback.objects.create(name=n,email=e,mobile=c,feedback=f)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)

def edit_profile(request):
    error=""
    data=User.objects.get(id=request.user.id)
    data2=Signup.objects.get(user=request.user)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        g = request.POST['gender']
        do = request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=do
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
        try:
            i=request.FILES['profilepic']
            data2.image=i
            data2.save()
            error="no"
        except:
            pass
    d={'data':data,'data2':data2,'error':error}
    return render(request,'edit_profile.html',d)

def view_feedback(request):
    data = Feedback.objects.all()
    d = {'data':data}
    return render(request,'view_feedback.html',d) 

def delete_feedback(request,id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')

def all_attendance(request):
    date = Record.objects.all()[::-1]
    data1 = User.objects.all()[::-1]
    data2 = Signup.objects.all()[::-1]
    data3 = Attendance.objects.all()[::-1]
    d = {'date':date,'data1':data1,'data2':data2,'data3':data3}
    return render(request,'all_attendance.html',d)



def present_user(request,id):
    data = User.objects.get(id=id)
    e = data.username
    data = Attendance.objects.filter(email__icontains=e)
    d = {'data':data}
    return render(request,'present_user.html',d)
