from django.contrib import admin
from backend.models import UserInfo

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
    list_filter = ('username', 'email', 'password')  # 过滤器
    search_fields = ('username', )  # 搜索字段
    date_hierarchy = 'update_time'  # 详细时间分层筛选　