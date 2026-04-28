from django.db import models
from activities.models import Event
# Create your models here.
class TicketCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    ticket_category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status= models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey('accounts.User',on_delete=models.CASCADE,related_name="ticket_created_by")

    def __str__(self):
        return self.ticket_number
