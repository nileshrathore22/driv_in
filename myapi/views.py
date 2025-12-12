from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Driving_Teacher
from .serializers import Driving_TeacherSerializer

# Create your views here.
@api_view(['GET'])
def home_page(request):
    return Response({"message": "Welcome to our Driving School Api!"})

@api_view(['GET'])
def get_teachers(request):
    teacher= Driving_Teacher.objects.all()
    serializer=Driving_TeacherSerializer(teacher, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_teacher(request):
    serializer=Driving_TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": " Teacher added!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_teacher(request,id):
    teacher=get_object_or_404(Driving_Teacher,id=id)
    serializer=Driving_TeacherSerializer(teacher)
    return Response(serializer.data)