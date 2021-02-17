from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^$',views.frontpage,name='front'),
    url(r'contact/$',views.contactpage,name='contact')
]
