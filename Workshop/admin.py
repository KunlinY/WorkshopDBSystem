from django.contrib import admin
from Workshop.models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('sNumber',)
    search_fields = ('sNumber',)

    def get_list_display(self, request):
        return ['sNumber']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ShopAdmin, self).get_search_results(request, queryset,search_term)
        return queryset, use_distinct


class ClassAdmin(admin.ModelAdmin):
    list_display = ('cNumber', 'cType', 'sNumber')
    search_fields = ('cNumber', 'cType', 'sNumber')

    def get_list_display(self, request):
        return ['cNumber', 'cType', 'sNumber']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ClassAdmin, self).get_search_results(request, queryset, search_term)

        return queryset, use_distinct


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eNumber', 'eName', 'eSex', 'eAge', 'position', 'cNumber', 'way', 'techGrading', 'dateOfAdmission')
    search_fields = ('eNumber', 'eName', 'eAge')

    def get_list_display(self, request):
        return ['eNumber', 'eName', 'eSex', 'eAge', 'position', 'cNumber', 'way', 'techGrading', 'dateOfAdmission']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(EmployeeAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pNumber', 'pName')
    search_fields = ('pNumber', 'pName')

    def get_list_display(self, request):
        return ['pNumber', 'pName']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ProductAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class DepotAdmin(admin.ModelAdmin):
    list_display = ('dNumber', 'dType')
    search_fields = ('dNumber', 'dType')

    def get_list_display(self, request):
        return ['dNumber', 'dType']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(DepotAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('pNumber', 'pName')
    search_fields = ('pNumber', 'pName')

    def get_list_display(self, request):
        return ['pNumber', 'pName']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ProviderAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('mNumber', 'pNumber', 'dNumber', 'dName', 'dPrice')
    search_fields = ('mNumber', 'pNumber', 'dNumber', 'dName', 'dPrice')

    def get_list_display(self, request):
        return ['mNumber', 'pNumber', 'dNumber', 'dName', 'dPrice']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(MaterialAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class WorkAdmin(admin.ModelAdmin):
    list_display = ('eNumber', 'wDate', 'wHours', 'wOvertime')
    search_fields = ('eNumber', 'wDate', 'wHours', 'wOvertime')

    def get_list_display(self, request):
        return ['eNumber', 'wDate', 'wHours', 'wOvertime']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(WorkAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class SalaryAdmin(admin.ModelAdmin):
    list_display = ('eNumber', 'sDate', 'sAmount', 'sSubsidy', 'sTotal')
    search_fields = ('eNumber', 'sDate', 'sAmount', 'sSubsidy', 'sTotal')

    def get_list_display(self, request):
        return ['eNumber', 'sDate', 'sAmount', 'sSubsidy', 'sTotal']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(SalaryAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class UsageAdmin(admin.ModelAdmin):
    list_display = ('cNumber', 'mNumber', 'uDate', 'uAmount')
    search_fields = ('cNumber', 'mNumber', 'uDate', 'uAmount')

    def get_list_display(self, request):
        return ['cNumber', 'mNumber', 'uDate', 'uAmount']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(UsageAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct


class ProduceAdmin(admin.ModelAdmin):
    list_display = ('cNumber', 'mNumber', 'pDate', 'pWeight', 'pUsed')
    search_fields = ('cNumber', 'mNumber', 'pDate', 'pWeight', 'pUsed')

    def get_list_display(self, request):
        return ['cNumber', 'mNumber', 'pDate', 'pWeight', 'pUsed']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ProduceAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct

admin.site.register(Shop, ShopAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Depot, DepotAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Usage, UsageAdmin)
admin.site.register(Produce, ProduceAdmin)
