from django.urls import path
from .views import shop_detail, delete_fr

urlpatterns = [

    path('shop-detail/<slug:name>/', shop_detail, name='shop-detail'),
    path('delete/fr/<slug:name>/', delete_fr, name='delete')

]
