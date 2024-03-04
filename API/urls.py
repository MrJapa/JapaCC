from django.urls import path
from .views import *

# urlpatterns = [
#     path('api/orders/', NyBestillingUpdateAPIView.as_view(), name='order-create'),
#     path('orders/<int:pk>/', NyBestillingUpdateAPIView.as_view(), name='order-update'),
    
# ]

urlpatterns = [
    path('orders/', create_order),
    path('api/orders/<int:pk>/', take_order, name='order-update'),
]