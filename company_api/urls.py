
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import CompanyViewset,EmployeeViewset

router = routers.DefaultRouter()
router.register(r'company',CompanyViewset)
router.register(r'employee',EmployeeViewset)

urlpatterns = [
    path('',include(router.urls))
   
]
