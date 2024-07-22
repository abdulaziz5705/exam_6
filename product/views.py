from django.shortcuts import render, redirect
from .models import Fruit, Vegetables, Meat, Bread
from .forms import FruitForm, VegetableForm, MeatForm, BreadForm


def shop_detail(request, name):
    if Vegetables.objects.filter(name=name):
        vegetable = Vegetables.objects.get(name=name)
        return render(request, 'shop-detail.html', {'product': vegetable})
    elif Fruit.objects.filter(name=name):
        fruit = Fruit.objects.get(name=name)
        return render(request, 'shop-detail.html', {'product': fruit})
    elif Meat.objects.filter(name=name):
        meat = Meat.objects.get(name=name)
        return render(request, 'shop-detail.html', {'product': meat})
    else:
        if Bread.objects.filter(name=name):
            bread = Bread.objects.get(name=name)
            return render(request, 'shop-detail.html', {'product': bread})


def delete_fr(request, name):
    if Fruit.objects.filter(name=name):
        fruit = Fruit.objects.get(name=name)
        fruit.delete()
        return redirect('shop')
    elif Vegetables.objects.filter(name=name):
        veg = Vegetables.objects.get(name=name)
        veg.delete()
        return redirect('shop')

    elif Meat.objects.filter(name=name):
        meat = Meat.objects.get(name=name)
        meat.delete()
        return redirect('shop')
    else:
        if Bread.objects.filter(name=name):
            bread = Bread.objects.get(name=name)
            bread.delete()
            return redirect('shop')


def fruit_create(request):
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
        else:
            return render(request, 'fruit_creat.html    ', {'form': form}, {'message': "Error!!!"})

    form = FruitForm()
    return render(request, 'fruit_creat.html', {'form': form})
