from django.db import models
from django.utils.translation import gettext_lazy as _


class WorkType(models.Model):
    '''
    業務形態モデル
    '''
    name = models.CharField(max_length=100, verbose_name=_("業務形態"))

    def __str__(self):
        return self.name


class CommmutingMethod(models.Model):
    '''
    通勤方法モデル
    '''
    method = models.CharField(max_length=20, verbose_name=_("通勤方法"))

    def __str__(self):
        return self.method


class Staff(models.Model):
    '''
    派遣スタッフモデル
    '''
    ycode = models.CharField(max_length=10, blank=True, null=True, verbose_name=_("Yコード"))
    username = models.CharField(max_length=50, verbose_name=_("通称"))
    kananame = models.CharField(max_length=50, verbose_name=_("カナ名"))
    tel = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("電話番号"))
    assign_company = models.CharField(max_length=100, verbose_name=_("派遣先"))
    group = models.CharField(max_length=100, verbose_name=_("所属"))
    work_content = models.CharField(max_length=100, verbose_name=_("業務内容"))
    work_type = models.ForeignKey(WorkType, on_delete=models.SET_NULL, null=True, verbose_name=_("業務形態"))
    billed_unit_price = models.PositiveIntegerField(verbose_name=_("請求単価"))
    pay_unit_price = models.PositiveIntegerField(verbose_name=_("支払単価"))
    contact_period = models.PositiveIntegerField(verbose_name=_("契約期間(ヶ月)"))
    commuting_method = models.ForeignKey(CommmutingMethod, on_delete=models.SET_NULL, null=True, verbose_name=_("通勤方法"))
    commuting_distance = models.FloatField(verbose_name=_("通勤距離(km)"))
    commuting_section = models.CharField(max_length=50, verbose_name=_("通勤区間"))
    commuting_start_date = models.DateField(verbose_name=_("通勤開始日"))
    commuting_expense = models.PositiveIntegerField(verbose_name=_("通勤費"))
    temp_staff_manager = models.CharField(max_length=50, verbose_name=_("派遣責任者"))
    temp_staff_leader = models.CharField(max_length=50, verbose_name=_("派遣指揮命令者"))
    ins_start_date = models.DateField(verbose_name=_("社会保険加入日"))
    remarks = models.TextField(blank=True, null=True, verbose_name=_("備考"))

    def __str__(self):
        return self.username
