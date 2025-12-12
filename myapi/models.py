from django.db import models

# Create your models here.
class Driving_Teacher(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    experience=models.IntegerField()
    contact_email=models.EmailField()
    
    def __str__(self):
        return self.name
