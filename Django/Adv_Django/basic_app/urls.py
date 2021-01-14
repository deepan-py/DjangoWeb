from django.conf.urls import url 
from basic_app import views

app_name = 'basic_app'

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

]
