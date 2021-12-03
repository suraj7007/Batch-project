from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.
def createbatch(request):
    return Response({"status":200, "msg":"Respose recieved"})