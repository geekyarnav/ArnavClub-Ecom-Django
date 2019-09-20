"""commerce URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from profiles import models
from profiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#ADD
#urlpatterns = [
#    path('',views.index),
#    path('addblog/',views.createblog)

urlpatterns = [
path('admin/', admin.site.urls),
#url(r'^$',views.home_view, name='home'),
path('', views.home_view , name='home'),
path('about/', views.about_view ,name='about'),
path('products/',views.products_view , name='products'),
path('contacts/',views.contact_view , name='contacts'),
path('services/',views.services_view ,name='services'),
# path('blogs/',views.blogs_view ,name='blogs'),
# path('addblog/',views.createblog ,name='addblog'),
]

urlpatterns += staticfiles_urlpatterns()