from a_app import views
from django.conf.urls import url 

app_name = 'a_app'

urlpattern = [
    url(r'^register',views.register,name='register'),
]