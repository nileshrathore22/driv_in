#from django.shortcuts import render 
from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import render 
# from sliderupdation.models import SliderUpdate
from contactdetail.models import Contactform
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def home_pagee(request): 
   return render(request,'index.html')
 
def about_page(request):
  return render(request,'about.html') 

#def contact_page(request):
  #return render(request,"contact.html")

def service_page(request):
  return render(request,"service.html")

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
   
   subject = f"Thank You for Contacting Us - {usersubject}"
   # Render HTML template
   html_content = render_to_string('email_template.html', {
    'username': username,
    'useremail': usermail,   # use usermail (not useremail) to match your form
    'usersubject': usersubject,
    'usermessage': usermessage,
})

   #message = (
      #f"Dear {username},\n\n"
      #f"Thank you for getting in touch with us at DriveSmart Academy!\n"
      #f"We’ve received your message:\n\n"
      #f"{usermessage},\n\n"
      #f"Our support team will review your query and get back to you as soon as possible.\n\n"
      #f"Drive safely and stay confident behind the wheel!\n\n"
      #f"Best Regards,\n"
      #f"DriveSmart Academy Support Team"
  #)
   
   #send_mail(
   # subject ="Testing mail",
   # message="Hello User! I hope you're doing great this time.",
   # from_email="sangamuniversity791@gmail.com",
    #recipient_list=["nileshrathore1522@gmail.com"],
   # fail_silently=False,
   #)
   # Plain text fallback
   text_content = (
    f"Dear {username},\n\n"
    "Thank you for reaching out to DriveSmart Academy!\n"
    "We’ve received your message and our support team will get back to you shortly.\n\n"
    "We appreciate your interest and look forward to helping you on your driving journey.\n\n"
    "Best regards,\n"
    "DriveSmart Academy Support Team"
)
   
# Send HTML email to user
   email = EmailMultiAlternatives(
    subject=subject,
    body=text_content,
    from_email="sangamuniversity791@gmail.com",  # ✅ must match EMAIL_HOST_USER
    to=[usermail],
)
   email.attach_alternative(html_content, "text/html")
   email.send(fail_silently=False)

   
  #send_mail(
      #subject =subject,
      #message=message,
      #from_email="sangamuniversity791@gmail.com",
      #recipient_list=[usermail],
      #fail_silently=False,
      #)
   admin_subject = f"New Contact Form Submission from {username}"
   admin_message = (
    f"New message received from the website contact form:\n\n"
    f"Name: {username}\n"
    f"Email: {usermail}\n"
    f"Subject: {usersubject}\n"
    f"Message:\n{usermessage}\n\n"
    f"Please review and respond promptly.\n\n"
    f"— DriveSmart Academy Website Notification"
  )
   admin_email = EmailMultiAlternatives(
    subject=admin_subject,
    body=admin_message,
    from_email="sangamuniversity791@gmail.com",  # ✅ must match EMAIL_HOST_USER
    to=["sangamuniversity791@gmail.com"],
)
   #admin_email.attach_alternative(html_content, "text/html")
   admin_email.send(fail_silently=False)
   #send_mail(
    #subject=admin_subject,
    #message=admin_message,
    #from_email="sangamuniversity791@gmail.com",
    #recipient_list=["sangamuniversity791@gmail.com"],
    #fail_silently=False,
#)

 
  return render(request,"contact.html", {'msg':msg})

def countriesData(request):
  api_url="https://api.first.org/data/v1/countries"
  
  response=requests.get(api_url)
  if response.status_code==200:
    countries_data = response.json()# Parse the JSON response
    countries = countries_data.get('data',{});# Extract;data&#39; key
  else:
    countries = {} # Handle the case where the API is not reachable
     # Pass the data to the template
  return render(request,'print_json.html',{'countries':countries}) #39;, {&#39;countries&#39;:
def driving_dashboard(request):

    # -------- API 1 : CAR DATA ----------
    car_api = "https://myfakeapi.com/api/cars/"
    try:
        r1 = requests.get(car_api, timeout=5)
        cars = r1.json().get("cars", [])
    except:
        cars = []

    # Normalize / fix missing year keys
    for c in cars:
        c["year"] = c.get("car_year") or c.get("car_model_year") or "N/A"

    context = {
        "cars": cars,
    }
    return render(request, "driving_dashboard.html", context)
