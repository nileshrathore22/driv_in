from django.shortcuts import render
from .models import Service, Course

def service_page(request):
    services = Service.objects.all()
    courses = Course.objects.all()
    return render(request, 'services.html', {'services': services, 'courses': courses})
