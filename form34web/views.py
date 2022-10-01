from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Region, Pdfpath
from rest_framework import viewsets, filters
from .serializers import PdfpathSerializer, RegionSerializer
from django.http import HttpResponse
# Create your views here.


class RegiontViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']


class PdfpathViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PdfpathSerializer
    queryset = Pdfpath.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id', 'form_34_path', 'polling_station_code']

