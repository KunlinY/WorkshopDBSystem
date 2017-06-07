# coding=utf-8
from django.shortcuts import render, render_to_response
from Workshop.models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse

#接受用户表单查询相应班组员工的考勤记录
def show_work(request):
    cNumber = request.POST.get('cNumber')
    employees = Employee.objects.filter(cNumber = cNumber)
    list = []
    print(cNumber)
    for employee in employees:
        works = Work.objects.filter(eNumber = employee.eNumber)
        temp_list = []
        temp_list.append(employee.eNumber)
        temp_list.append(employee.eName)
        for work in works:
            temp_list.append(work.wDate)
            temp_list.append(work.wHours)
            temp_list.append(work.wOvertime)
        list.append(temp_list)
    return render_to_response('show.html', {'posts': list},
                                            RequestContext(request))

def show_salary(request):#这里面要定义好各个内容对应的工资部分
    cNumber = request.POST.get('cNumber')
    class_type = Class.objects.filter(cNumber = cNumber)
    employees = Employee.objects.filter(cNumber = cNumber)
    list = []
    print(cNumber)
    for employee in employees:
        salarys = Salary.objects.filter(eNumber = employee.eNumber)
        for salary in salarys:
            temp_list = []
            temp_list.append(employee.eNumber)
            temp_list.append(employee.eName)
            temp_list.append(salary.sDate)
            temp_list.append(employee.position)
            temp_list.append(class_type)
            temp_list.append(salary.sAmount)
            temp_list.append(salary.sSubsidy)
            temp_list.append(salary.sTotal)
        list.append(temp_list)
    return render_to_response('input.html', {'posts': list},
                              RequestContext(request))

def show_payment(request):
    if request.method != 'POST':
        providers = Provider.objects.all()
        list = sub_showpayment(providers)
    else:
        pNumber = request.POST.get('pNumber')
        providers = Provider.objects.filter(pNumber = pNumber)
        list = sub_showpayment(providers)
    return render_to_response('', {'posts': list},
                              RequestContext(request))  # 填对应的html


def sub_showpayment(providers):
    list = []
    for provider in providers:
        temp_list2 = []
        materials = Material.objects.filter(pNumber=provider.pNumber)
        for material in materials:
            temp_list1 = []
            usages = Usage.objects.filter(mNumber=material.mNumber)
            for usage in usages[:-1]:
                temp_list1.append(provider.pNumber)
                temp_list1.append(provider.pName)
                temp_list1.append(material.mNumber)
                temp_list1.append(material.dName)
                temp_list1.append(material.dPrice)
                temp_list1.append(Usage.uDate)
                temp_list1.append(Usage.uAmount)
                break;
            temp_list2.append(temp_list1)
        list.append(temp_list2)
    return list









