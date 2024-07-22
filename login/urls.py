from django.urls import path
from .views import login_view, regester_view, account, log_out_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('regester/', regester_view, name='regester'),
    path('account/', account, name='account'),
    path('logout/', log_out_view, name='log_out')
]
