from django.contrib import admin
from backend.models import UserInfo, RankInfo, EmployeeInfo, DepInfo

from django.contrib import admin
from backend.models import UserInfo, RankInfo, EmployeeInfo, DepInfo

# Register your models here.

# admin.site.register(UserInfo)
# admin.site.register(UserType)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'status', 'create_time', 'update_time')
    list_per_page = 20
    ordering = ('-create_time',)
    list_display_links = ('username', 'password', )
    # 筛选器
    list_filter = ('username', 'email', 'status')  # 过滤器
    search_fields = ('username', 'email' )  # 搜索字段
    date_hierarchy = 'update_time'  # 详细时间分层筛选　


class EmployeeInfofor(admin.TabularInline):
    model = EmployeeInfo
    # raw_id_fields = ("rank_id","department_id")


@admin.register(DepInfo)
class DepInfoAdmin(admin.ModelAdmin):
    model = DepInfo
    inlines = [EmployeeInfofor,]
    list_display = ('id', 'department_name', 'status', 'comments', 'create_time', 'update_time')
    list_per_page = 20
    ordering = ('-create_time',)
    list_display_links = ('department_name',)
    list_filter = ('department_name', 'status')  # 过滤器
    search_fields = ('department_name', 'status')  # 搜索字段
    date_hierarchy = 'update_time'  # 详细时间分层筛选　


@admin.register(RankInfo)
class RankInfoAdmin(admin.ModelAdmin):
    model = RankInfo
    inlines = [EmployeeInfofor,]
    list_display = ('id', 'rank_name', 'status', 'comments', 'create_time', 'update_time')
    list_per_page = 20
    ordering = ('-create_time',)
    list_display_links = ('rank_name',)
    list_filter = ('rank_name', 'status')  # 过滤器
    search_fields = ('rank_name', 'status')  # 搜索字段
    date_hierarchy = 'update_time'  # 详细时间分层筛选　


class aaadmin(admin.ModelAdmin):
    list_display = ['rank__name',]


# @admin.register(EmployeeInfo)
# class EmployeeInfoAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'employee_name', 'email', 'rank_id', 'department_id', 'phone', 'status', 'comments',
#         'create_time',
#         'update_time')
#     list_per_page = 50
#     ordering = ('-create_time',)
#     list_display_links = ('employee_name',)
#     list_filter = ('employee_name', 'rank_id', 'department_id', 'phone', 'email')  # 过滤器
#     search_fields = ('employee_name', 'rank_id', 'department_id', 'phone', 'email')  # 搜索字段
#     date_hierarchy = 'update_time'  # 详细时间分层筛选

admin.site.site_header = 'CMS后台管理系统'
admin.site.site_title = 'Company Manage System'