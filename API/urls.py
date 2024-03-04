from django.urls import path
from .views import NyBestillingUpdateAPIView

urlpatterns = [
    path('orders/<int:pk>/', NyBestillingUpdateAPIView.as_view(), name='order-update'),
    
]