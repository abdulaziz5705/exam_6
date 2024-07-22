from django.contrib import admin
from .models import Fruit, Vegetables, Meat, Bread, Turi


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'turi']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Vegetables)
class VegetablesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Meat)
class MeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ['id', 'turi']
    list_display_links = ['turi']
    search_fields = ['turi']
