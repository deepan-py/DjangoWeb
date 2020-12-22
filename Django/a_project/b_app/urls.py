from django.conf.urls import url
from b_app import views

urlpatterns = [
    url(r'^$',views.index,name='b_app')
]