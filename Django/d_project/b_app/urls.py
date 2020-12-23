from b_app import views
from django.conf.urls import url 

app_name = 'b_app'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^others/$',views.others,name='others'),
    url(r'^basic/$',views.basic,name='basic'),
    url(r'^relative$', views.relURL,name='relative')
]
