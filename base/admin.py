from django.contrib import admin
from django.contrib.auth.models import Group

from base.models import SiteUser, Department, WorkType, CommutingMethod

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
    

class CommutingMethodAdmin(admin.ModelAdmin):
    list_display = ("method",)
    search_fields = ("method",)  

admin.site.register(SiteUser)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(CommutingMethod, CommutingMethodAdmin)
admin.site.unregister(Group)  # Groupモデルを管理画面から削除
