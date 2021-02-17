from django.conf.urls import url 
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$',views.frontpage,name='front'),
    url(r'contact/$',views.contactpage,name='contact')
]
