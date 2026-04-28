from django.urls import path,include
from accounts.views import UserViewSet,LoginMixin
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"users",UserViewSet,basename="user")
urlpatterns = [
    path("",include(router.urls)),
    path('login/', LoginMixin.as_view(), name='login'),
  
]
