
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import CafeViewSet

router = routers.DefaultRouter()
router.register(r'cafe',CafeViewSet)

urlpatterns = [
    path('',include(router.urls))
   
]
