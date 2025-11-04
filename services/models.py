from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.IntegerField()

    def __str__(self):
        return self.name
