from django.db import models
from django.utils import timezone

class Category(models.Model):
    catname = models.CharField(max_length=250)

    def __str__(self):
        return self.catname


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    datetime_post = models.DateTimeField(default=timezone.now)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # ✅ Add this line

    def __str__(self):
        return self.title
