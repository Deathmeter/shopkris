"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
       url(r'^$', ListView.as_view(queryset=Articles.object.all().order_by("-date") [:20],
       template_name="news/posts.html")),
       url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Articles, template_name="news/post.html")),
]
