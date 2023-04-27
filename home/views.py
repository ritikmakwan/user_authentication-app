from django.shortcuts import render,redirect
from .models import Emp
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def home(request):
    e=Emp.objects.all()
    return render(request,"index.html",{"e":e})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect("/signup")
        elif password!=rpassword:
            messages.info(request,'Password mismatch')
            return redirect("/signup")
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            messages.info(request,"successfully signup")
            return redirect("/")
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid username or password")
            return redirect("/login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")