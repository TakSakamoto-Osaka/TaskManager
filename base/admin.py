from django.contrib import admin
from django.contrib.auth.models import Group

from base.models import SiteUser, Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')


admin.site.register(SiteUser)
admin.site.register(Department, DepartmentAdmin)
admin.site.unregister(Group)  # Groupモデルを管理画面から削除
