from django.shortcuts import render
from .models import Filter


def index(request):
    items = Filter.objects.all()
    filter_type = request.GET.get('type')
    filter_brand = request.GET.get('brand')

    if filter_type:
        items = items.filter(type=filter_type)

    if filter_brand and filter_type:
        items = items.filter(brand=filter_brand, type=filter_type)

    if filter_brand:
        items = items.filter(brand=filter_brand)

    return render(request, 'olx/index.html', {'items': items})

def detail(request, pk):
    item = Filter.objects.get(id=pk)
    return render(request, 'olx/detail.html', {'item': item})