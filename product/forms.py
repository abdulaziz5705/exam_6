from .models import Fruit, Vegetables, Meat, Bread
from django import forms


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'turi', 'price', 'foydalari']

    def is_valled(self):
        pass


class VegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetables
        fields = ['name', 'description', 'turi', 'price', 'foydalari']


class MeatForm(forms.ModelForm):
    class Meta:
        model = Meat
        fields = ['name', 'description', 'turi', 'price', 'foydalari']


class BreadForm(forms.ModelForm):
    class Meta:
        model = Bread
        fields = ['name', 'description', 'turi', 'price', 'foydalari']


