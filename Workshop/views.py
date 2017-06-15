# coding=utf-8
from django.shortcuts import render_to_response
from Workshop.models import *
from django.template import RequestContext
import datetime

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
    return render_to_response('show_work.html', {'posts': list},
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
            temp_list.append(work_year(salary.sDate, employee.dateOfAdmission))
            temp_list.append(position_salary(employee.position))
            temp_list.append(class_type)
            temp_list.append(salary.sAmount)
            temp_list.append(salary.sSubsidy)
            temp_list.append(salary.sTotal)
            list.append(temp_list)
    return render_to_response('show_salary.html', {'posts': list},
                              RequestContext(request))

def show_payment(request):
    if request.method != 'POST':
        providers = Provider.objects.all()
        list = sub_showpayment(providers)
    else:
        pNumber = request.POST.get('pNumber')
        providers = Provider.objects.filter(pNumber = pNumber)
        list = sub_showpayment(providers)
    return render_to_response('show_payment.html', {'posts': list},
                              RequestContext(request))

def show_produce(request):#输入date和可选项class
    cNumber = request.POST.get('cNumber')
    date = request.POST.get('pDate')
    if cNumber == None:
        classes = Class.objects.all()
        list = sub_showproduce(classes, date)
    else:
        classes = Class.objects.filter(cNumber = cNumber)
        list = sub_showproduce(classes, date)
    return render_to_response('show_produce.html', {'posts': list},
                              RequestContext(request))

def show_product_lead(request):#输入产品号和日期
    pNumber = request.POST.get('pNumber')
    date = request.POST.get('pDate')
    classes = Produce.objects.filter(pNumber = pNumber)
    product = Product.objects.filter(pNumber = pNumber)
    for product_in in product:
        pName = product_in.pName
    list = []
    for class_in in classes:
        employees = Employee.objects.filter(cNmuber = class_in.cNumber)
        for employee in employees:
            temp_list = []
            if(check_work(employee, date)):
                temp_list.append(employee.eNumber)
                temp_list.append(employee.eName)
                temp_list.append(employee.cNumber)
                temp_list.append(class_in.cType)
                temp_list.append(pName)
            list.append(temp_list)
    return render_to_response('show_product_lead.html', {'posts': list},
                              RequestContext(request))

def show_outrate(request):
    date= request.POST.get('pDate') #"GET"要小写成"get"
    produces = Produce.objects.filter(pDate = date)
    list = []
    list_material = []
    list_preprocess = []
    list_hotprocess = []
    list_spices = []
    list_wrap = []
    list_rice = []
    list_product = []
    for produce in produces:
        print(type(produce.cNumber.cNumber))
        classes = Class.objects.filter(cNumber=produce.cNumber.cNumber)
        for class_in in classes:
            if(class_in.cType == '原料组'):
                list_material.append(detail(produce, class_in, date))
            elif(class_in.cType == '前处理组'):
                list_preprocess.append(detail(produce, class_in, date))
            elif (class_in.cType == '热厨组'):
                list_hotprocess.append(detail(produce, class_in, date))
            elif (class_in.cType == '调料组'):
                list_spices.append(detail(produce, class_in, date))
            elif (class_in.cType == '包装组'):
                list_wrap.append(detail(produce, class_in, date))
            elif (class_in.cType == '米饭组'):
                list_rice.append(detail(produce, class_in, date))
            elif (class_in.cType == '产品组'):
                list_product.append(detail(produce, class_in, date))
            break;
    list.append(list_material)
    list.append(list_preprocess)
    list.append(list_hotprocess)
    list.append(list_spices)
    list.append(list_wrap)
    list.append(list_rice)
    list.append(list_product)
    return render_to_response('show_outrate.html', {'posts': list},
                              RequestContext(request))


def position_salary(position):
    if(position=='无'):
        return 0
    elif(position=='车间主任'):
        return 2000
    elif(position=='车间管理人员'):
        return 1000
    else:
        return 500

def work_year(time,dtime):
    return (time-dtime).year

def sub_showpayment(providers):
    list = []
    for provider in providers:
        temp_list2 = []
        materials = Material.objects.filter(pNumber=provider.pNumber)
        for material in materials:
            temp_list1 = []
            usages = Usage.objects.filter(mNumber=material.mNumber)
            for usage in usages[::-1]:
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

def sub_showproduce(classes, date):
    list = []
    for class_in in classes:
        produces = Produce.objects.filter(cNumber = class_in.cNumber, pDate = date)
        for produce in produces:
            temp_list = []
            products = Product.objects.filter(pNumber = produce.pNumber.pNumber)
            for product in products:
                temp_list.append(class_in.cNumber)
                temp_list.append(class_in.cType)
                temp_list.append(produce.pWeight)
                if(class_in.cType == '产品组'):
                    temp_list.append(product.pName)
                    temp_list.append(produce.pNumber)
                break;
            list.append(temp_list)
    return list;

def check_work(employee, date):
    flag = 0
    works = Work.objects.filter(eNumber = employee.eNumber)
    for work in works:
        flag = 1
        break;
    return flag

def detail(produce, class_in, date):
    list = []
    list.append(class_in.cNumber)
    list.append(class_in.cType)
    list.append(produce.pUsed)
    list.append(produce.pWeight)
    list.append((1.0 * produce.pWeight/produce.pUsed))
    return list
