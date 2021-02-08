from django.db import models
from django.utils.html import format_html

# Create your models here.
class Tower(models.Model):
    num = models.CharField(max_length=16)
    catalog = models.CharField(max_length=64)
    vender = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    comment = models.CharField(max_length=128)
    def detail_button(self):
        btn_str="<a class='btn btn-xs' href='{}'>详情</a>"
        return format_html(btn_str, '/admin/tower/excel/?q=%s'%str(self.id))
    detail_button.short_description = '详情'
    def __str__(self):
        return self.num
    
class Excel(models.Model):
    name = models.CharField(max_length=16)
    tower = models.ForeignKey(Tower,on_delete=models.CASCADE)
    def detail_button(self):
        btn_str="<a class='btn btn-xs' href='{}'>详情</a>"
        return format_html(btn_str, '/admin/tower/sheet/?q=%s'%str(self.id))
    detail_button.short_description = '详情'
    def __str__(self):
        return self.name
    
class Sheet(models.Model):
    name = models.CharField(max_length=16)
    excel = models.ForeignKey(Excel,on_delete=models.CASCADE)
    def detail_button(self):
        btn_str="<a class='btn btn-xs' href='{}'>详情</a>"
        return format_html(btn_str, '/admin/tower/tajixingnengcanshu/?q=%s'%str(self.id))
    detail_button.short_description = '详情'
    def __str__(self):
        return self.name
    
class TaJiXingNengCanShu(models.Model):
    excel = models.ForeignKey(Excel,on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheet,on_delete=models.CASCADE)
    r = models.CharField(max_length=16)
    r_max = models.CharField(max_length=16)
    c_max = models.CharField(max_length=16)
    n_25 = models.CharField(max_length=16)
    n_30 = models.CharField(max_length=16)
    n_35 = models.CharField(max_length=16)
    n_40 = models.CharField(max_length=16)
    n_45 = models.CharField(max_length=16)
    n_50 = models.CharField(max_length=16)
    n_55 = models.CharField(max_length=16)
    n_60 = models.CharField(max_length=16)
    n_65 = models.CharField(max_length=16)
    n_70 = models.CharField(max_length=16)