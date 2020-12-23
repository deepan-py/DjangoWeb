from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'b_app/index.html')

def basic(request):
    return render(request,'b_app/base.html')

def others(request):
    return render(request,'b_app/others.html')

def relURL(request):
    return render(request,'b_app/reUrl.html')