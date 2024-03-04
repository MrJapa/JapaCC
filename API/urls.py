from django.urls import path
from .views import NyBestillingUpdateAPIView

urlpatterns = [
    path('nybestilling/<int:pk>/', NyBestillingUpdateAPIView.as_view(), name='order-update'),
    
]