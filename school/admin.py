from django.contrib import admin

# Register your models here.

from school.models import students, access


class Syudents1(admin.ModelAdmin):
    list_display = ['name', 'sex', 'address', 'no']


admin.site.register(students, Syudents1)


class Students2(admin.ModelAdmin):
    list_display = ['create_timme', 'no', 'results']


admin.site.register(access,Students2)
admin.site.site_header = '学生管理后台系统'
admin.site.site_title = '学生表'
