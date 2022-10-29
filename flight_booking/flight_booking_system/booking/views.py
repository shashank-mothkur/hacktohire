from django.shortcuts import render,HttpResponse
from django.urls import reverse
from datetime import datetime
from .models import *
# Create your views here.
def base(request):
    return render(request,"booking/base.html")

def login_view(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        num=request.POST.get("number")
        k=LoginPage(user_name=name,user_email=email,user_password=password,user_number=num)
        k.save()

    return  render(request,"booking/login.html")

def flight_details(request):
    if request.method=="POST":
        roundtrip=request.POST.get()
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
        name=request.POST.get("name")
