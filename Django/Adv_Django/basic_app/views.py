from django.shortcuts import render
from django.views.generic import View, TemplateView 
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
