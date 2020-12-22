"""a_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from a_app import views
from b_app import views as v
urlpatterns = [
    url(r'^$',views.ans,name='index'),
    url(r'^a_app/',include('a_app.urls')),
    url(r'^b_app/',include('b_app.urls')),
    url(r'^asd/',v.anotherIndex,name='index'),
    path('root/', admin.site.urls),
]
