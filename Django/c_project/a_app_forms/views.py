from django.shortcuts import render
from . import forms
# ? the above method is to search in same level folder use of '..' search one level up
# !the other method of importing forms

# * from a_app_forms import forms 
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form=forms.Formname()
    if request.method=='POST':
        form = forms.Formname(request.POST)
        if form.is_valid():
            # Do something
            print("Validation Success!!!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['emailId'])
            print(form.cleaned_data['option_select'])
            # the above print will print 1 or 2 or 3 as value as given in forms.py
        # else:
        #     print("BOT")
    return render(request,'basicapp/form_page.html',{'form':form})