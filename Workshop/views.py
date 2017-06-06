# coding=utf-8
from django.shortcuts import render_to_response, render
from Workshop.models import Employee

def show(request):
    employee_list = Employee.objects.all
    return render(request, 'show.html', {'employee':employee_list})
# Create your views here.
