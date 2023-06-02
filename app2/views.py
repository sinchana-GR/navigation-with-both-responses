from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bheem(request):
    return HttpResponse('this is chota bheem page')
def chutki(request):
    return render(request,'chutki.html')