# Django
## Requirements
*django, rest framework*
<hr>
To create project

```shell
django-admin startproject <projectName>
cd <projectName>
python manage.py startapp <appName>
```
Then add apps to `settings.py`, add the below lines to `INSTALLED_APPS`

```python
'<appName>',
'rest_framework',
'rest_framework.authtoken',
```
### `urls.py`  
Just a basic<br>
`Project folder` `urls.py`
```python
from django.conf.urls import url, include  # add this line

urlpatterns = [
    url('',include('appName.urls',namespace='appName'))  # add this line
]
```
Then in `app folder` create `urls.py` file
```python
from django.conf.urls import url
from . import views
app_name = 'appName'  # same as the name given in the namespace
urlpatterns = [
    url(r'/$',views.page,name='page'),  # the name='page' is used in template taging
]
```
### Templates and Static files
we can create templates and static folder in project folder or in app folder 

**Project folder**<br>
create `templates`and `static` folder in `project Folder` <br>
add the `templates` and `static` to `settings.py`

```python
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')  # for django==2.2
TEMPLATE_DIR =  BASE_DIR / 'templates'  # for django==3.1
STATIC_DIR = os.path.join(BASE_DIR,'static')
STATIC_DIR = BASE_DIR / 'static' 
# the below lines is common for both django==2.2 and django==3.1
TEMPLATES = [{'DIRS':[TEMPLATE_DIR,]}]
STATICFILES_DIRS = [
    STATIC_DIR,
]
```
**App Folder**<br>
just create `templates` and `static` folder no need to add in  `settings.py` as the `TEMPLATES` and `INSTALLED_APPS` variable will take care of that.

### `views.py`
under app folder `views.py` 
```python
from django.http import request
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponse
```
every imports has it's own use `request, render, HttpResponse` are used in `function based views`
```python
def index(request):
    return render(request,'index.html',{'insert_me':'Something to display but display as texts it will not convert to html code '})

def anotherIndex(request):
    return HttpResponse("<b>It is bold</b>")
```
**Class Based Views:**<br>
***TemplateView:***<br>
```python
class AboutView(TemplateView):
    template_name = 'appFolder/*.html'
    # def get(self,request):
    #     return render(request,'appFolder/*.html',{})
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['insert_me'] = 'BasicInjection'
        return context
```
***ListView:***<br>
```python
class SchoolListView(ListView):
    model = Post
    context_object_name = 'schools'  # this is used in html file for viewing
    # if the above is not mentioned then the default is 'school_list'
    # if template name not given it will take it as 'school_list.html'

class PostListView(ListView):
    # template_name = 'posts.html'
    model = Post

    # sql query
    # lte is less than or equal to
    # field lookups in documnentation
    # ? https://docs.djangoproject.com/en/3.1/topics/db/queries/
    # * files__lookuptype=value eg:- published_date__lte=timeone.now()
    # * which is equals to the following sql query
    # ? SELECT * FROM Post WHERE published_date <= CURDATE() ORDER BY published_date;

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
```
***DetailView:***<br>
Same as `ListView`

***CreateView:***<br>
```python
class SchoolCreateView(CreateView):
    fields = ['name','principal','location']
    model = models.School
    # this will look for template name 'school_form.html' that is the moelname_form.html in our case the modelname is school lowercaps
 
class StudentCreateView(CreateView):
    fields = ['school','name','age']
    model = models.Student
    # here it is 'student_form.html'
```
***UpdateView:***<br>
same as `CreateView`

***DeleteView:***<br>
```python
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    # the list is the name given in the urls.py
```
### `urls.py`
Below are some of the examples of urls
```python
app_name = 'appName'
urlpatterns = [
    
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    # the 'pk' is primary key unique identifier for each record in database in which python will know it as id for the database the id is used in school_list.html for viewing of record of each student under school
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    # Below url will cause an error if above url is comment out as it does not as it does not specifies the id of the database
    # url(r'^[d+]/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^createSchool/$',views.SchoolCreateView.as_view(),name='createSchool'),
    url(r'^createStudent/$', views.StudentCreateView.as_view(), name='createStudent'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    url(r'^post/(?P<pk>\d+)/publish$',views.post_publish,name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comments_to_post,name='add_comment_to_post'),
    url(r'^comments/(?P<pk>\d+)/approve/$',views.comment_approved,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.comment_publish,name='comment_publish'),
]
```
## `models.py`<br>
Some model example
```python
from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=250)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('appOne.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.text
```
## `forms.py`<br>
we need to create `forms.py` in app Folder<br>
example
```python
from django.db.models.fields import CharField
from django import forms
from .models import formsApp

class FormApp(forms.ModelForm):
    class Meta():
        model = formsApp
        fields = '__all__'
        widgets = {
            'email_Id': forms.TextInput(attrs={'placeholder':'Enter Email'}),
            'DateOfBirth': forms.TextInput(attrs={'type':'date','placeholder':'yyyy-mm-dd'}),
            'gender_radio':forms.RadioSelect(),
        }
```
this form is from `models.py`
```python
from django.db import models
from django.utils.html import mark_safe, escape
# from django import forms
# Create your models here.
gender_choices = (
    ('M','Male'),
    ('F','Female'),
)

multichoice = (
    ('1','one'),
    ('2','two'),
    ('3','three')
)

class formsApp(models.Model):
    first_name = models.CharField(max_length=256,blank=True,default='00000')
    last_name = models.CharField(max_length=256)
    email_Id = models.EmailField(max_length=512,unique=True)
    phone_number = models.IntegerField(default=5)
    DateOfEntry = models.DateField(auto_now_add=True)
    DateOfBirth = models.DateField(null=True)
    DateTimeOfEntry = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1,choices=gender_choices)
    gender_radio = models.CharField(choices=gender_choices, max_length=1,default='M')
    imgesAdd = models.ImageField(upload_to = 'templates/images',blank=True)
    filesUpload = models.FileField(upload_to='templates/files',blank=True)
```
this `views.py`
```python
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
```

##  `admin.py`<br>
```python
from django.contrib import admin
from .models import formsApp
# Register your models here.
# the below code is to show images in admin panel
# for this we need to change settings.py as well and urls.py
@admin.register(formsApp)
class model1Admin(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html("<img src='{}' />".format(obj.imgesAdd.url))
    image_tag.short_description = 'Image'
    readonly_fields = ['image_tag']
```
## `urls.py`
In `settings.py` add `MEDIA_URL='/media/'` and `MEDIA_ROOT = os.path.join(BASE_DIR,'media')`
then
```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from formss import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^formapp', views.formsapp,name='formapp'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this line is used to get url to view the image in admin panel
```