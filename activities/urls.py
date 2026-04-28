from django.urls import path,include
from rest_framework.routers import DefaultRouter
from activities.views import VenueViewSet,EventViewSet,EventCategoryViewSet
router=DefaultRouter()
router.register(r"event-categories",EventCategoryViewSet,basename="event-categories")
router.register(r"venues",VenueViewSet,basename="venues")
router.register(r"events",EventViewSet,basename="events")

urlpatterns = [
    path("",include(router.urls))
  
]
