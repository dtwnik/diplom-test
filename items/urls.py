from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'CPU', CPUViewSet)
router.register(r'MB', MBViewSet)
router.register(r'Ram', RamViewSet)
router.register(r'Storage', StorageViewSet)
router.register(r'GPU', GPUViewSet)
router.register(r'PSU', PSUViewSet)

urlpatterns = [
    path('', include(router.urls)),
]