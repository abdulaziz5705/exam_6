from django.urls import path
from .views import shop_detail, delete_fr, fruit_create, veg_create, bread_create, meat_create

urlpatterns = [

    path('shop-detail/<slug:name>/', shop_detail, name='shop-detail'),
    path('delete/fr/<slug:name>/', delete_fr, name='delete'),
    path('fruit/create/', fruit_create, name='fruit-create'),
    path('veg/create/', veg_create, name='veg-create'),
    path('meat/create/', meat_create, name='meat-create'),
    path('bread/create/', bread_create, name='bread-create')

]
