from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I'm from view.py under a_app used in template folder &nbsp", 'something':"<b> it's not changing something</b>"}
    return render(request,'a_app/index.html',context=my_dict)
    
def ans(kjdc):
    return HttpResponse("<b>display it</b>")

