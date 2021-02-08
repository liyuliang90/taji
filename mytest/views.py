from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import City

def choose_city(request):
    province_id = request.GET.get('p')
    result = {
        'code':200
    }
    if province_id:
        city_set = City.objects.filter(province__id=province_id)
        city = []
        for i in city_set:
            city.append({'id':i.id, 'name': i.name})
        result['data'] = city
    else:
        result['code'] = 201
    return JsonResponse(result,safe=False)