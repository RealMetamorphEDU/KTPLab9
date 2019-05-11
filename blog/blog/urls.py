"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from articles import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.archive, name='archive'),
    url(r'^admin/', admin.site.urls),
    url(r'^article/(?P<article_id>\d+)/$', views.get_article, name='get_article'),
    url(r'^article/new/', views.create_post, name='create_post'),
    url(r'^registration/', views.create_user, name='create_user'),
    url(r'^auth/', views.input_user, name='input_user'),
]
