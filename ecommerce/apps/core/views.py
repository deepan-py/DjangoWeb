from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request,'core/front.html',{})

def contactpage(request):
    return render(request,'core/contact.html',{})