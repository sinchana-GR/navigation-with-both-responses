from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tom(request):
    return HttpResponse('hai tom')
def jerry(request):
    return render(request,'jerry.html')