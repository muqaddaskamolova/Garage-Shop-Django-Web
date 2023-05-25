from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    # path('', ProductListView.as_view, name='product_list'),
    path('', all_products, name='all_products'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', category_list, name='category_list'),
    path('category/<int:category_id>/', category_list, name='category'),
    path('category/<slug:slug>/', category_list, name='category_detail'),
    path('shop/', shop, name='shop'),
]
