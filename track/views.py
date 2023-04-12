from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class CompanyView(ListCreateAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.all()