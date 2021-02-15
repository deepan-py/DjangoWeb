from django.conf.urls import url 
from store import views

urlpatterns = [
    url(r'^$',views.store,name='store'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),

]
