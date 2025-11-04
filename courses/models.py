from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200) # or 'title'
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    level = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
def __str__(self):
    return self.title
