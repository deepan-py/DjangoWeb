from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'b_app/index.html',context_dict)

def basic(request):
    return render(request,'b_app/base.html')

def others(request):
    return render(request,'b_app/others.html')

def relURL(request):
    return render(request,'b_app/reUrl.html')