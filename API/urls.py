from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', create_order),
    path('orders/<int:pk>/', take_order, name='order-update'),
    path('orders/accept/<int:pk>/', accept_order, name='order-accept'),
]