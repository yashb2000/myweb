"""
URL configuration for webemp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login),
    path('newemp/',views.newemp),
    path('addemp/',views.addemp),
    path('searchno/',views.searchno),
    path('allemp/',views.allemp),
    path('updsal/',views.updsal),
    path('changesal/',views.changesal),
    path('delemp/',views.delemp),
    path('delete/',views.delete),
    path('elist/',views.elist),
    path('searchfilm/',views.searchfilm),
    path('searchfilmonid/',views.searchfilmonid),
    path('takecity/',views.takecity),
    path('showweather/',views.showweather),




]
