from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def masha(request):
    return HttpResponse('this is masha page')
def bear(request):
    return render(request,'bear.html')