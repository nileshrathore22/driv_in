from django.db import models

# Create your models here.
class Contactform(models.Model):
    username=models.CharField(max_length=500)
    usermail=models.CharField(max_length=250)
    usersubject=models.CharField(max_length=500)
    usermessage=models.TextField()
    usersubject=models.FileField(upload_to="media")
    #submitdate=models.DateTimeField(auto_now_add=True, default=timezone.now)
    