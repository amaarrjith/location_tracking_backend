from django.db import models

# Create your models here.

class location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    location = models.TextField()
    date = models.DateField((""), auto_now=False, auto_now_add=False)
    time = models.TimeField()
    
    def __str__(self):
        return self.location
    