from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from odata_api.models import *
from odata_api.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers    