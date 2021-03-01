from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_manage_library(request):
    return HttpResponse("Czesc!")