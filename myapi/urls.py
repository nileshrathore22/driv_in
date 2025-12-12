from django.urls import path
from . import views
urlpatterns=[
    path('', views.get_teachers,name='get_teachers'),
    path('add/',views.add_teacher,name='add_teacher'),
    path('<int:id>/',views.get_teacher,name='get_teacher'),
]