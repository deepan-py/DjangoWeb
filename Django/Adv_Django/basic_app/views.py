from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                                CreateView, UpdateView, DeleteView)
from . import models
# from django.http import HttpResponse

# Create your views here.
# Below is a function based views
# def index(request):
#     return render(request,'index.html')

# --------- Class Based Views ------------------

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based View !!! displayed from views.py file under basic_app")


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectMe'] = 'Basic Injection'
        return context

# ---------------------------------------------------------------------

class SchoolListView(ListView):  # ListView it helps to link to html file
    #! It changes the School to small letters 
    #! and change to "school_list" -----------> Which is used in the scl_list.html file in for loop by defalut to change it
    context_object_name = 'schools'
    model = models.School
    # as the template_name is not mentioned here so the file name should be 'school_list.html'

class SchoolDetailView(DetailView):
    # by default it uses just lowercase as 'school' it does not add school_detail like previous
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/scl_details.html'

class SchoolCreateView(CreateView):
    # this will look for template name 'school_form.html' that is the moelname_form.html in our case the modelname is school lowercaps
    fields = ['name','principal','location']
    model = models.School
 
class StudentCreateView(CreateView):
    fields = ['school','name','age']
    model = models.Student

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = models.School 