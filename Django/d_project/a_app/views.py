from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'a_app/index.html')

def other(request):
    return render(request,'a_app/other.html')

def basic(request):
    return render(request,'a_app/base.html')

def relUrl(request):
    return render(request,'a_app/relURLTemplate.html')