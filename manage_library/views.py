from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# TODO decorator of log in
def main_manage_library(request):
    pass
    return render(request, template_name="manage_library/main_manage_library.html")
