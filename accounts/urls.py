from django.urls import path, include

from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('customer/', views.createCustomer, name= 'createCustomer'),
    path('orders/', views.createOrder, name="orders"),
    path('orders/<int:pk>/', views.updateOrder, name='updateOrder'),
    path('ordersDelete/<int:pk>', views.deleteOrder, name="deleteOrder")
]