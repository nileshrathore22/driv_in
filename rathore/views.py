#from django.shortcuts import render 
from django.http import HttpResponse
from django.shortcuts import render 
# from sliderupdation.models import SliderUpdate
from contactdetail.models import Contactform
from django.core.mail import send_mail

def home_pagee(request): 
   return render(request,'index.html')
 
def about_page(request):
  return render(request,'about.html') 

def contact_page(request):
  return render(request,"contact.html")

#def service_page(request):
  #return render(request,"service.html")

def schedule_page(request):
  return render(request,"schedule.html")


def contact_page(request):
  msg=''
  if request.method=='POST':
   username=request.POST.get('username')
   usermail=request.POST.get('usermail')
   usersubject=request.POST.get('usersubject')
   usermessage=request.POST.get('usermessage')  
   allData=Contactform(username=username,usermail=usermail,usersubject=usersubject,usermessage=usermessage)
   allData.save()
   msg='form submitted!' 
   
   #send_mail(
   # subject ="Testing mail",
   # message="Hello User! I hope you're doing great this time.",
   # from_email="sangamuniversity791@gmail.com",
    #recipient_list=["nileshrathore1522@gmail.com"],
   # fail_silently=False,
   #)
   send_mail(
    subject ="Testing mail",
    message="Hello User! I hope you're doing great this time.",
    from_email="sangamuniversity791@gmail.com",
    recipient_list=["nileshrathore1522@gmail.com"],
    fail_silently=False,
   )
   
 
  return render(request,"contact.html", {'msg':msg})