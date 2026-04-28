from django.db import models
from accounts.models import User
# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    updated_at = models.DateTimeField(auto_now=True)
    hoster=models.ForeignKey(User,related_name='events_hosters', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    