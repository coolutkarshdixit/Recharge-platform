from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import ContactW
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app1.models import ContactP
from django.contrib import sessions

# Create your views here.
def home(request):
    return render(request,'index.html')
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,"register.html")
def login1(request):
    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    return render(request,'index.html')

def message(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        message=request.POST.get("message")
        t=name+email+contact+message
        r=ContactW(name=name, email=email, contact=contact, message=message)
        r.save()
        return render(request,"contact.html",{"msg":"Value Inserted"})


def registeruser(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        #t=fname+lname+email+password
        #return HttpResponse(t)
        try:
            r=User.objects.create_user(first_name=fname, last_name=lname, email=email, username=email, password=password)
            r.save()
            return render(request,"register.html",{'msg':'A/C Created!!'})
        except:
            return render(request,"register.html",{'msg':'Old User !!'})
        
        
def userhome(request):
    return render(request,'userhome.html')


def loginuser(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=authenticate(username=email, password=password)
        if user is not None:
            request.session["uemail"]=email
            #return HttpResponse("Login")
            login(request,user)
            return redirect('/userhome')
        else:
            return HttpResponse("Sorry!! Wrong Email or Password")
        

def homeuser(request):
    r=ContactP.objects.all()
    return render(request,'homeuser.html',{'data':r}) 
    

def recharge(request):
    return render(request,'recharge.html')
       