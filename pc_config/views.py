from rest_framework import viewsets

from .models import *
from .serializer import *


class BuildViewSet(viewsets.ModelViewSet):
    queryset = build.objects.all()
    serializer_class = BuildSerializer