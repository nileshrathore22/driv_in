from django.db import models

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.client_name
