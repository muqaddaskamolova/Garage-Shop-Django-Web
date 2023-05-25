from django.urls import path
from .views import *

app_name = 'basket'

urlpatterns = [
    path('', basket_summary, name='basket_summary'),
    path('checkout/', basket_checkout, name='basket_checkout'),
    path('add/', basket_add, name='basket_add'),
    path('delete/', basket_delete, name='basket_delete'),
    path('update/', basket_update, name='basket_update'),
]
