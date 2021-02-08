from django.contrib import admin
from .models import Tower, Excel, Sheet, TaJiXingNengCanShu

# Register your models here.
class TowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'catalog', 'vender', 'description', 'comment', 'detail_button']
    
class ExcelAdmin(admin.ModelAdmin):
    search_fields = ['tower__id']
    list_display = ['id', 'tower', 'name', 'detail_button']
    
class SheetAdmin(admin.ModelAdmin):
    search_fields = ['excel__id']
    list_display = ['id', 'excel', 'name', 'detail_button']

class TaJiXingNengCanShuAdmin(admin.ModelAdmin):
    change_form_template = 'sheet_choose.html'
    search_fields = ['excel__id']
    list_display = ['r', 'r_max', 'c_max', 'n_25', 'n_30', 'n_35', 'n_40', 'n_45', 'n_50', 'n_55', 'n_60', 'n_65', 'n_70']
    
admin.site.register(Tower,TowerAdmin)
admin.site.register(Excel,ExcelAdmin)
admin.site.register(Sheet,SheetAdmin)
admin.site.register(TaJiXingNengCanShu,TaJiXingNengCanShuAdmin)