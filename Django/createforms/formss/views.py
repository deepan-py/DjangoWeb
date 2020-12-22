from django.shortcuts import render
from .formssss import FormApp
# Create your views here.

def index(request):
    return render(request,'index.html')


def formsapp(request):
    form = FormApp()
    print(1)
    if request.method=="POST":
        print(2)
        form = FormApp(request.POST, request.FILES)
        if form.is_valid():            
            form.save(commit=True)
            print(3)
            return index(request)
        else:
            print('Error in form Submission')
    return render(request,'forms.html',{'form':form})
