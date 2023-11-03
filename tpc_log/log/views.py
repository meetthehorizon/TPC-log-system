from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def logview(request):
    return HttpResponse("wait for the log sheet")