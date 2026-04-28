from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket
from utils import generate_code


@receiver(post_save, sender=Ticket)
def generate_ticket_code(sender, instance, created, **kwargs):
    if created:
        instance.code = generate_code()
        instance.save()

