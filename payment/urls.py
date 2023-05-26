from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns = [path('', BasketView, name='basket'),
               path('orderplaced/', order_placed, name='order_placed'),
               path('error/', Error.as_view(), name='error'),
               path('webhook/', stripe_webhook),
               ]
