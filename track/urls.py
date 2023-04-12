from django.urls import include, path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'device', DeviceViewSet)
router.register(r'checkout', CheckoutViewSet)
router.register(r'device-log', DeviceLogViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
