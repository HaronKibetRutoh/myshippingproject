from django.db import models
from django.conf import settings


class Quote(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    luggage_type = models.CharField(max_length=50)
    luggage_weight = models.CharField(max_length=20)
    luggage_dimensions = models.CharField(max_length=50)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    mode = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'self.name'

class Shopping(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'self.name'