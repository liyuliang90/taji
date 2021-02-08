from django.db import models
from django.utils.html import format_html
# Create your models here.
class Persion(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class A(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=100)

class B(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=990)
    a = models.ForeignKey(A,on_delete=models.CASCADE)
    def pass_audit_str(self):
        parameter_str = 'id={}&status={}'.format(str(self.id), str(self.name))
        color_code = ''
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="通过审核"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="通过审核">' \
                  '</a>'
        return format_html(btn_str, '/admin/mytest/a/')
    pass_audit_str.short_description = '通过审核'
    
    
class Province(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=16)
    provice = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)