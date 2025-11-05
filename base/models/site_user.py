from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    '''
    部署情報
    '''
    DEP_TYPES = (
        ('HEAD', '本社'),
        ('SATELLITE', '事務所'),
    )
    
    name = models.CharField('部署名', max_length=100)
    type = models.CharField('部署タイプ', max_length=20, choices=DEP_TYPES)

    class Meta:
        verbose_name = '部署'
        verbose_name_plural = '部署一覧'

    def __str__(self):
        return self.name


class SiteUser(AbstractUser):
    '''
    サイトユーザー情報
    '''
    department = models.ForeignKey(Department, verbose_name='部署', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'サイトユーザー'
        verbose_name_plural = 'サイトユーザー一覧'
        
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('top')
