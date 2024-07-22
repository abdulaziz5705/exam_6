from django.shortcuts import render
from product.models import Fruit, Vegetables, Meat, Bread


def index_view(request):
    fruit = Fruit.objects.all()
    vegetable = Vegetables.objects.all()
    meat = Meat.objects.all()
    bread = Bread.objects.all()
    return render(request, 'index.html', {'fruit': fruit, 'vegetable': vegetable, 'meat': meat, 'bread': bread})


def base_view(request):
    return render(request, 'base.html')


def cart_view(request):
    return render(request, 'cart.html')


def chackout_view(request):
    return render(request, 'chackout.html')


def contact_view(request):
    return render(request, 'contact.html')


def shop_detail_view(request):
    return render(request, 'shop-detail.html')


def shop_view(request):
    fruit = Fruit.objects.all()
    vegetable = Vegetables.objects.all()
    meat = Meat.objects.all()
    bread = Bread.objects.all()
    return render(request, 'shop.html', {'fruit': fruit, 'vegetable': vegetable, 'meat': meat, 'bread': bread})


def testimonial_view(request):
    return render(request, 'testimonial.html')


def error_view(request):
    return render(request, '404.html')
