from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view
from API.views import NyBestillingUpdateAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('logout/', logout_view, name='logout'),
    path('manage/', views.manage_view, name='manage'),
    path('Restaurant/<str:Navn>/', views.restaurant_detail, name='restaurant_detail'),
    path('Restaurant/<str:Navn>/checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.orders_view, name='orders'),
    path('nybestilling/<int:pk>/', NyBestillingUpdateAPIView.as_view(), name='nybestilling-update'),
]