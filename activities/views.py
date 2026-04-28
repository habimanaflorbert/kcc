from rest_framework import viewsets
from activities.models import Event, EventCategory, Venue
from activities.serializers import EventSerializer, EventCategorySerializer, VenueSerializer
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from datetime import datetime
from accounts.permissions import IsAdmin, BaseAuthPermission

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes=[BaseAuthPermission]

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [BaseAuthPermission()]
