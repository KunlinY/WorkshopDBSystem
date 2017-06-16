# coding=utf-8
from django.db import models
from django.core.exceptions import ValidationError


def validate_num(num):
    if num < 0:
        raise ValidationError("请输入正数！")


class Shop(models.Model):
    objects = models.Manager()
    sNumber = models.AutoField(
        primary_key=True, verbose_name='车间号', db_index=True
    )

    class Meta:
        verbose_name = '车间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '车间 %s' % self.sNumber


class Class(models.Model):
    objects = models.Manager()
    cNumber = models.AutoField(
        primary_key=True, verbose_name='班组号', db_index=True
    )
    cType = models.CharField(
        max_length=10, verbose_name='班组类型',
        choices=(
            ('原料组', '原料组'),
            ('前处理组', '前处理组'),
            ('热厨组', '热厨组'),
            ('调料组', '调料组'),
            ('包装组', '包装组'),
            ('米饭组', '米饭组'),
            ('产品组', '产品组')
        )
    )
    sNumber = models.ForeignKey(
        Shop, verbose_name='车间号'
    )

    class Meta:
        verbose_name = '班组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '班组 %s' % self.cNumber


class Employee(models.Model):
    objects = models.Manager()
    eNumber = models.AutoField(
        primary_key=True, verbose_name='员工号', db_index=True
    )
    eName = models.CharField(
        max_length=10, verbose_name='员工姓名'
    )
    eSex = models.CharField(
        choices=(('男', '男'), ('女', '女')), verbose_name='性别', max_length=5
    )
    eAge = models.IntegerField(
        verbose_name='员工年龄', validators=[validate_num]
    )
    position = models.CharField(
        max_length=20, verbose_name='岗位',
        choices = (
            ('车间主任', '车间主任'),
            ('车间管理人员', '车间管理人员'),
            ('班长', '班长'),
            ('普通职工', '普通职工')
        )
    )
    way = models.CharField(
        max_length=10, verbose_name='用工方式',
        choices = (
            ('小时工', '小时工'),
            ('劳务工', '劳务工')
        )
    )
    techGrading = models.CharField(
        max_length=10, verbose_name='技术评级',
        choices=(
            ('无', '无'),
            ('高级', '高级'),
            ('中级', '中级'),
            ('普通', '普通')
        ),
        default='无'
    )
    dateOfAdmission = models.DateField(
        verbose_name='入职时间'
    )
    cNumber = models.ForeignKey(
        Class, verbose_name='班组号'
    )

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.eNumber, self.eName)


class Product(models.Model):
    objects = models.Manager()
    pNumber = models.AutoField(
        primary_key=True, verbose_name='产品号', db_index=True
    )
    pName = models.CharField(
        max_length=20, verbose_name='产品名'
    )

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.pNumber, self.pName)


class Depot(models.Model):
    objects = models.Manager()
    dNumber = models.AutoField(
        primary_key=True, verbose_name='仓库号', db_index=True
    )
    dType = models.CharField(
        max_length=10, verbose_name='仓库类型',
        choices = (
            ('产品仓库', '产品仓库'),
            ('原料仓库', '原料仓库')
        )
    )

    class Meta:
        verbose_name = '仓库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.dNumber, self.dType)


class Provider(models.Model):
    objects = models.Manager()
    pNumber = models.AutoField(
        primary_key=True, verbose_name='供应商号', db_index=True
    )
    pName = models.CharField(
        max_length=20, verbose_name='供应商名'
    )

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.pNumber, self.pName)


class Material(models.Model):
    objects = models.Manager()
    mNumber = models.AutoField(
        primary_key=True, verbose_name='原料号', db_index=True
    )
    pNumber = models.ForeignKey(
        Provider, verbose_name='供应商号'
    )
    dNumber = models.ForeignKey(
        Depot, verbose_name='仓库号'
    )
    dName = models.CharField(
        max_length=20, verbose_name='原料名'
    )
    dPrice = models.FloatField(
        verbose_name='原料单价', validators=[validate_num]
    )

    class Meta:
        verbose_name = '原料'
        verbose_name_plural = verbose_name
        unique_together = ('mNumber', 'dNumber')

    def __str__(self):
        return '%s %s' % (self.mNumber, self.dPrice)


class Work(models.Model):
    objects = models.Manager()
    eNumber = models.ForeignKey(
        Employee, verbose_name='考勤员工', db_index=True
    )
    wDate = models.DateField(
        verbose_name='日期'
    )
    wHours = models.IntegerField(
        verbose_name='正常工作时数', validators=[validate_num]
    )
    wOvertime = models.IntegerField(
        verbose_name='加班时数', default=0, validators=[validate_num]
    )

    class Meta:
        verbose_name = '考勤'
        verbose_name_plural = verbose_name
        unique_together = ('eNumber', 'wDate')

    def __str__(self):
        return '%s %s' % (self.eNumber, self.wDate)


class Salary(models.Model):
    objects = models.Manager()
    eNumber = models.ForeignKey(
        Employee, verbose_name='员工号', db_index=True
    )
    sDate = models.DateField(
        verbose_name='日期'
    )
    sAmount = models.IntegerField(
        verbose_name='计件产量', default=0, validators=[validate_num]
    )
    sSubsidy = models.IntegerField(
        verbose_name='全勤补贴', default=0, validators=[validate_num]
    )
    sTotal = models.IntegerField(
        verbose_name='工资合计', default=0, validators=[validate_num]
    )

    class Meta:
        verbose_name = '应收工资'
        verbose_name_plural = verbose_name
        unique_together = ('eNumber', 'sDate')

    def __str__(self):
        return '%s %s %s' % (self.sDate, self.eNumber, self.sTotal)


class Usage(models.Model):
    objects = models.Manager()
    cNumber = models.ForeignKey(
        Class, verbose_name='班组号'
    )
    mNumber = models.ForeignKey(
        Material, verbose_name='原料号', db_index=True
    )
    uDate = models.DateField(
        verbose_name='日期'
    )
    uAmount = models.IntegerField(
         verbose_name='使用量', validators=[validate_num]
    )

    class Meta:
        verbose_name = '原料使用'
        verbose_name_plural = verbose_name
        unique_together = ('cNumber', 'mNumber', 'uDate')

    def __str__(self):
        return '%s' % self.uAmount


class Produce(models.Model):
    objects = models.Manager()
    cNumber = models.ForeignKey(
        Class, verbose_name='班组号', db_index=True
    )
    pNumber = models.ForeignKey(
        Product, verbose_name='产品号', blank=True, default=None
    )
    dNumber = models.ForeignKey(
        Depot, verbose_name='仓库号', blank=True, default=None
    )
    pDate = models.DateField(
        verbose_name='日期'
    )
    pWeight = models.IntegerField(
        verbose_name='当日产品重量', default=0, validators=[validate_num]
    )
    pUsed = models.IntegerField(
        verbose_name='当日原料使用重量', default=0, validators=[validate_num]
    )

    class Meta:
        verbose_name = '产品生产'
        verbose_name_plural = verbose_name
        unique_together = ('cNumber', 'pNumber', 'pDate')

    def __str__(self):
        return '%s %s' % (self.pDate, self.pWeight)


