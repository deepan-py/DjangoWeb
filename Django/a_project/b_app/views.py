from django.shortcuts import render
from django.http import HttpResponse
from b_app.models import AccessRecord, Topic, Webpage
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # mydict = {'insert_me':'Something under b_app'}
    return render(request,'b_app/index.html',context=date_dict)

def anotherIndex(request):
    return HttpResponse("Something will apperar from b_app views.py")