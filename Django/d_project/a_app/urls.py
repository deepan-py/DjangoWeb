from django.conf.urls import url 
from a_app import views


# this is used in relURLTemplate.html
app_name = 'a_app'

# the name='other' this is ude in tempalte taging of
urlpatterns = [
    url(r'^basic/$',views.basic,name='basic'),
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relUrl,name='relative'),
]
