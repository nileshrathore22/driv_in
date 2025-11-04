from django.contrib import admin
from .models import Service, Course

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'fee')
