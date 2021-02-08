from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Sheet

def choose_sheet(request):
    excel_id = request.GET.get('excel_id')
    result = {
        'code':200
    }
    if excel_id:
        sheet_set = Sheet.objects.filter(excel__id=excel_id)
        sheet = []
        for i in sheet_set:
            sheet.append({'id':i.id, 'name': i.name})
        result['data'] = sheet
    else:
        result['code'] = 201
    return JsonResponse(result,safe=False)