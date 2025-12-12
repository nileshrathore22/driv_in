from rest_framework import serializers
from .models import Driving_Teacher

class Driving_TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driving_Teacher
        fields= '__all__'