# coding=utf-8
from django.shortcuts import render, render_to_response
from Workshop.models import *
from django.template import loader, Context
from django.http import HttpResponse



def show_work(request):
    posts = Shop.objects.all()
    print(posts)
    return render_to_response('show.html', {'posts': posts})
