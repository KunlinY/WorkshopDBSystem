# coding=utf-8
"""WorkshopDBSystem URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
import Workshop.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show_work/', Workshop.views.show_work),
    url(r'^show_salary/', Workshop.views.show_salary),
    url(r'^show_payment/', Workshop.views.show_payment),
    url(r'^show_produce/', Workshop.views.show_produce),
    url(r'^show_product_lead/', Workshop.views.show_product_lead),
    url(r'^show_outrate/', Workshop.views.show_outrate),
    url(r'^update_salary/', Workshop.views.update_salary)
]
