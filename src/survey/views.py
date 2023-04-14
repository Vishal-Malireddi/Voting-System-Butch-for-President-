from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# a basic hello world text view
def index(request):
    return HttpResponse("Hello world. You are at the survey index.")

