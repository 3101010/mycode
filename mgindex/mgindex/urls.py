"""mgindex URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from mainapp import views as mainapp_views

urlpatterns = [
    url(r'^$', mainapp_views.index),
    url(r'^login/', mainapp_views.login),
    url(r'^logout/', mainapp_views.logout),
    url(r'^noperm', mainapp_views.noperm),
    url(r'^daohang/', mainapp_views.daohang),
    url(r'^assets_links/', mainapp_views.assets_links),
    url(r'^assets_list/', mainapp_views.assets_list),
    url(r'^user/manage$',mainapp_views.user_manage),
    url(r'^register/',mainapp_views.register),
    url(r'^admin/', admin.site.urls),
    url(r'^user/(?P<uid>[0-9]+)/$',mainapp_views.user),
    url(r'^api/user/(?P<id>[0-9]+)/$',mainapp_views.user_detail),
]
