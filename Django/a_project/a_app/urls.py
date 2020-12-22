from django.conf.urls import url
from a_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^ans$',views.ans,name='index')
]