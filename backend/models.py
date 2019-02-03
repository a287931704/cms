from django.db import models
from backend.managers import *
from django.contrib import admin

class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class UserInfo(BaseTable):
    class Meta:
        verbose_name = '用户信息'
        db_table = 't_user_info'

    username = models.CharField('用户名', max_length=100, null=False)
    password = models.CharField('密码', max_length=100, null=False)
    email = models.EmailField('邮箱', null=True)
    phone = models.CharField('电话', max_length=100)
    status = models.IntegerField('有效1/无效0', default=1)
    objects = UserInfoManager()

class DepInfo(BaseTable):
    class Meta:
        verbose_name = '部门信息'
        db_table = 't_dep_info'

    department_name = models.CharField('部门名称', max_length=100, unique=True, null=False)
    status = models.IntegerField('有效1/无效0', default=1)
    comments = models.CharField('备注', max_length=100, null=True)
    objects = DepInfoManager()

class RankInfo(BaseTable):
    class Meta:
        verbose_name = '职级信息'
        db_table = 't_rank_info'

    rank_name = models.CharField('职级名称', max_length=100, unique=True, null=False)
    status = models.IntegerField('有效1/无效0', default=1)
    comments = models.CharField('备注', max_length=100, null=True)
    objects = RankInfoManager()

class EmployeeInfo(BaseTable):
    class Meta:
        verbose_name = '员工信息'
        db_table = 't_employee_info'

    employee_name = models.CharField('员工姓名', max_length=100, null=False)
    department = models.ForeignKey(DepInfo, on_delete=models.DO_NOTHING)
    rank= models.ForeignKey(RankInfo, on_delete=models.DO_NOTHING)
    email = models.EmailField('邮箱', null=True)
    phone = models.CharField('电话', max_length=100)
    status = models.IntegerField('有效1/无效0', default=1)
    comments = models.CharField('备注', max_length=100, null=True)
    objects = EmployeeInfoManager()

