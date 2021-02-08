from django.contrib import admin
from django.forms import Form,ModelForm
# Register your models here.
from django import forms
from .models import Persion, A,B, Province, City, Member
'''
class BInline(admin.StackedInline):
    model = B
'''
class BInline(admin.TabularInline):
    model = B
    can_delete = False
    fields = ('name','age' )
    readonly_fields = ( 'name','age')
    verbose_name = ('name')
    verbose_name_plural = ('name')
    extra = 0
    def has_add_permission(self, request, obj=None):
        """ 不允许这个inline类增加记录 (当然也增加不了，readonly_fileds中定义的字段，在增加时无法输入内容) """
        return False

class AAdmin(admin.ModelAdmin):
    inlines = [BInline, ]
    
class BAdmin(admin.ModelAdmin):
    list_display = ['name', 'pass_audit_str']
    search_fields = ("name",)
        
class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ("name",)
    #autocomplete_fields = ['city',]
    
    change_form_template = 'city_form.html'
    '''
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "city":
            kwargs["queryset"] = City.objects.filter(province__id=1)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    '''
admin.site.register(Persion)
admin.site.register(A, AAdmin)
admin.site.register(B,BAdmin)
admin.site.register(Province)
admin.site.register(City,CityAdmin)
admin.site.register(Member,MemberAdmin)
