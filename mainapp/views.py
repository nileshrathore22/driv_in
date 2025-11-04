from django.shortcuts import render
from courses.models import Course
from team.models import TeamMember
from testimonial.models import Testimonial

def index(request):
    courses = Course.objects.all()[:3]           # Show top 3 courses
    team_members = TeamMember.objects.all()[:4]  # Show top 4 team members
    testimonials = Testimonial.objects.all()[:3] # Show top 3 testimonials

    return render(request, 'index.html', {
        'courses': courses,
        'team_members': team_members,
        'testimonials': testimonials,
    })
